from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Address




@login_required(login_url='/accounts/login/')
def checkout(request):
    address = Address.objects.filter(user = request.user)
    context={
        'address' : address
    }
    return render(request,'order/checkout.html',context)