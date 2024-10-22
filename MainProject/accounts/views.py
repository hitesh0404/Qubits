from django.shortcuts import render

# Create your views here.


def register(request):
    context = {
        'page_name' : 'Register'
    }
    return render(request,'accounts/register.html',context)