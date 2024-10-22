from django.shortcuts import render

# Create your views here.

from .models import Brand
def brandlist(request):
    data = Brand.objects.all()
    return render(request,'product/brandlist.html',{'data':data})