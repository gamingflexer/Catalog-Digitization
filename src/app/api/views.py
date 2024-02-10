from django.http import HttpResponse
from django.template import loader

def catalouge_page(request):
  template = loader.get_template('catalouge.html')
  return HttpResponse(template.render())

def single_product(request):
  template = loader.get_template('product_single.html')
  return HttpResponse(template.render())