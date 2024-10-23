from django.shortcuts import render

# Create your views here.


def register(request):
    context = {
        'page_name' : 'Register'
    }
    print('Hello Django here ')
    return render(request,'accounts/register.html',context)

def login(request):
    context = {
        'page_name' : 'Log In'
    }
    return render(request,'accounts/login.html',context)
