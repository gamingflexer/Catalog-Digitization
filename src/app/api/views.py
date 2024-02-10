from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Record
from django.contrib import messages
from .serializers import ProductSerializer
from django.http import JsonResponse
import os
from config import BASE_PATH

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
            image_path = os.path.join(BASE_PATH,'app','main',settings.STATIC_ROOT, 'images', image_name)
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            # Process the uploaded image and get product details
            # product_detail = get_data_openai(image_path)
            # product_details.append(product_detail)
        
        # Handle audio recording
        if 'audio_data' in request.POST:
            # Save the audio data locally
            audio_data = request.POST['audio_data']
            audio_path = os.path.join(settings.STATIC_ROOT, 'audio', 'recorded_audio.wav')
            with open(audio_path, 'wb') as f:
                f.write(audio_data)
            # Process the uploaded image and get product details
            # product_detail = get_data_openai(image_path)
            # product_details.append(product_detail)
        # Dummy data for testing - You can replace this with actual data retrieved from the AI model
        product_details  = []
        dummy_data = [
            {'barcode': '123456', 'brand': 'Brand A', 'manufactured_by': 'Manufacturer A', 'product_name': 'Product A', 'weight': 1.5, 'variant': 'Variant A', 'net_content': '100ml', 'price': 10.0, 'parent_category': 'Category A', 'child_category': 'Subcategory A', 'description': 'Description for Product A', 'quantity': 100, 'mrp': '20.0'},
            {'barcode': '654321', 'brand': 'Brand B', 'manufactured_by': 'Manufacturer B', 'product_name': 'Product B', 'weight': 2.0, 'variant': 'Variant B', 'net_content': '200ml', 'price': 15.0, 'parent_category': 'Category B', 'child_category': 'Subcategory B', 'description': 'Description for Product B', 'quantity': 200, 'mrp': '25.0'}
        ]
        product_details.extend(dummy_data)
        return JsonResponse(dummy_data[0], safe=False)  # Return product details as JSON response
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