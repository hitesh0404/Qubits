from django.shortcuts import render
from django.contrib.auth.decorators import login_required





@login_required(login_url='/accounts/login/')
def checkout(request):
    context={

    }
    return render(request,'order/checkout.html',context)