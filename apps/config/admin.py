from django.contrib import admin
from .models import CompanyInfo, ServiceModel, Info

# Register your models here.

admin.site.register(CompanyInfo)
admin.site.register(ServiceModel)
admin.site.register(Info)