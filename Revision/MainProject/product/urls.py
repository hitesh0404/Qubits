from django.urls import path
from . import views
urlpatterns =[
    path('brand-list',views.brandlist,name='brandlist')
]