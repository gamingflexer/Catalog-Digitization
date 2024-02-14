from django.urls import path
from . import views
from .views import ProductAPIView,SearchProducts,TotalNumberOfProducts,ProductDetailsById,UpdateProduct

urlpatterns = [
    path('', views.catalouge_page, name='index'),
    path('product/<int:product_id>/', views.product_page, name='product_detail'),
    path('product-voice/<int:product_id>/', views.edit_voice_product, name='voice_product_detail'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('upload/', views.upload_image_and_audio, name='add_product_by_image'),
    path('api/products/', ProductAPIView.as_view(), name='product_api'),
    path('api/delete_product/<int:product_id>/', views.delete_product_api, name='delete_product_api'),
    
    path('api/search_products/', SearchProducts.as_view(), name='search_products'),
    path('api/total_number_of_products/', TotalNumberOfProducts.as_view(), name='total_number_of_products'),
    path('api/product_details/<int:pk>/', ProductDetailsById.as_view(), name='product_details_by_id'),
    path('api/update_product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
]