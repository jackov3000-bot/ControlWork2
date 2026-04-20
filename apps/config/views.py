from django.shortcuts import render
from .models import CompanyInfo, ServiceModel, Info

def index(request):
    company = CompanyInfo.objects.first()
    services = ServiceModel.objects.all()
    return render(request, "index.html", locals())
def contact(request):
    company = CompanyInfo.objects.first()
    return render(request, "contact.html", locals())
def trtr(request):
    info = Info.objects.first()
    return render(request, "trtr.html", locals())

# Create your views here.
