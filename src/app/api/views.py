from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Database
from .serializers import ProductSerializer,DatabaseSerializer
from django.http import JsonResponse
import os
from config import BASE_PATH
from api.module.product_description import get_details
from django.views.decorators.http import require_http_methods
from django.db.models import Q

def catalouge_page(request):
    # Fetch all products from the database
    products = Product.objects.all()
    for product in products:
        if product.images_paths:
            # Split the images_paths string and get the URL of the first image
            image_urls = product.images_paths.split(',')
            product.first_image_url = image_urls[0] if image_urls else None
        else:
            product.first_image_url = None
    context = {
        'products': products
    }
    return render(request, 'catalouge.html', context)

  
def product_page(request, product_id):
    product = Product.objects.get(pk=product_id)
    if product.images_paths:
        product.images_paths = product.images_paths.split(",")
    return render(request, 'product_page.html', {'product': product})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        # Update the product fields with the submitted data
        product.barcode = request.POST.get('barcode')
        product.brand = request.POST.get('brand')
        product.sub_brand = request.POST.get('sub_brand')
        product.manufacturer = request.POST.get('manufacturer')
        # Update other fields similarly
        
        # Save the updated product
        product.save()
        
        # Redirect to the product page after saving
        return HttpResponseRedirect(reverse('product_detail', args=(product.id,)))

    return render(request, 'edit_product.html', {'product': product})
  
def catalouge_page(request):
    # Fetch all products from the database
    products = Product.objects.all()

    # Handle search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(product_name__icontains=query)

    for product in products:
        if product.images_paths:
            # Split the images_paths string and get the URL of the first image
            image_urls = product.images_paths.split(',')
            product.first_image_url = image_urls[0] if image_urls else None
        else:
            product.first_image_url = None

    context = {
        'products': products,
        'search_query': query  # Pass the search query to display in the search bar
    }
    return render(request, 'catalouge.html', context)
  
def upload_image_and_audio(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        for image in images:
            # Save the image locally in the static directory
            image_name = image.name
            image_path = os.path.join(BASE_PATH,'app','main',settings.MEDIA_ROOT, 'images', image_name)
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
        print('Image saved at:', image_path)
        input_data = get_details(image_path)
        static_img_path = "http://34.122.223.224:9002/media/images/" + image_name
        product_data = {
            'brand': input_data.get('brand',None),
            'mrp': input_data.get('mrp',None),
            'quantity': input_data.get('quantity',None),
            'parent_category': input_data.get('parent_category',None),
            'manufactured_by': input_data.get('manufactured_by', ''),
            'product_name': input_data.get('type_of_product',None),
            'images_paths': static_img_path,  # Static path after saving image
            'description': input_data.get('description',None)  
        }
        
        # Create a new Product instance and save to database
        product = Product.objects.create(**product_data)
        return JsonResponse(product_data, safe=False)  # Return product details as JSON response
    return render(request, 'upload_image.html')
  
class ProductAPIView(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
def edit_voice_product(request,product_id):
    if request.method == 'POST':
        # Handle voice file submission here
        voice_file = request.FILES.get('voice_file')
        if voice_file:
            # Save the voice file to a specific location or process it as needed
            # For example, you can save it to the media directory
            # Assuming you have a media directory configured in your Django settings
            with open('media/voice_files/' + voice_file.name, 'wb') as f:
                for chunk in voice_file.chunks():
                    f.write(chunk)
            return JsonResponse({'message': 'Voice file submitted successfully.'})
        else:
            return JsonResponse({'error': 'No voice file submitted.'}, status=400)
    else:
        return render(request, 'edit_voice_product.html')
    
def delete_product_api(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return HttpResponseRedirect(reverse('index'))
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)
    
class SearchProducts(APIView):
    def get(self, request):
        name = request.query_params.get('name', '')
        products = Database.objects.filter(Q(product_name__icontains=name) & Q(description__icontains=name))
        db_serializer = DatabaseSerializer(products, many=True)
        return Response(db_serializer.data)

class TotalNumberOfProducts(APIView):
    def get(self, request):
        count = Database.objects.count()
        return Response({"total_number_of_products": count})

class ProductDetailsById(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)