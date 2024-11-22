from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from accounts.models import Address
# @login_required(login_url='/accounts/login/')
class Checkout(View):
    # @login_required
    def get(self,request):
        address = Address.objects.filter(user = request.user)
        context={
            'address' : address
        }
        return render(request,'order/checkout.html',context)
    # @login_required
    def post(self,request):
        address_id= request.POST.get('address')
        if address_id:
            request.session['address_id'] = address_id
            return redirect('proceed_to_pay')
        else:
            return redirect('ceckout')
        
        
def proceed_to_pay(request):

    return render(request,'order/proceed_to_pay.html')
