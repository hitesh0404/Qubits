from django.contrib import admin

# Register your models here.
from .models import (Product,HsnCode,Category,Brand,ProductImages)
 
admin.site.register([Product,HsnCode,Category,Brand,ProductImages])
admin.site.site_header='My Site'
admin.site.site_title='My Page'