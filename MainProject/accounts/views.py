from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.views import View

def register(request):
    if request.method == 'GET':
        print(' GET method')
        context = {
        'page_name' : 'Register'
        }
        return render(request,'accounts/register.html',context)

    elif request.method == 'POST':
        
        print(' POST request')
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = User.objects.create_superuser(username=username,password=password)
        print(user)
        return redirect('/') 
    
class Register(View):
    
    def get(self,request):
        print(' GET method')
        context = {
        'page_name' : 'Register'
        }
        return render(request,'accounts/register.html',context)

    def post(self,request):
        print(' POST request')
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = User.objects.create_superuser(username=username,password=password)
        print(user)
        return redirect('/')
  




def login(request):
    context = {
        'page_name' : 'Log In'
    }
    return render(request,'accounts/login.html',context)
