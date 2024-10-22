from django.shortcuts import render
from .models import Brand
# Create your views here.
def brand_list(request):
    data= Brand.objects.all()
    context ={
        'brands' : data
    }
    return render(request,'product/brand_list.html',context)