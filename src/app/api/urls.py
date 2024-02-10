from django.urls import path
from . import views
from .views import ProductAPIView

urlpatterns = [
    path('', views.catalouge_page, name='index'),
    path('product/<int:product_id>/', views.product_page, name='product_detail'),
    path('product-voice/<int:product_id>/', views.edit_voice_product, name='voice_product_detail'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('upload/', views.upload_image_and_audio, name='add_product_by_image'),
    path('api/products/', ProductAPIView.as_view(), name='product_api'),
]