from django.shortcuts import render
from django.shortcuts import render
from .models import Houses

# Create your views here.
def home_page(request):
    view = Houses.objects.all()
    context = {
        'view': view
    }
    return render(request, 'agency/index.html', context)

def add_house(request):
    return Httpresponse("<h1>create a listing</h1>")

def house_detail(request):
    return Httpresponse("<h1>view details</h1>")

def update_house(request):
    return Httpresponse("<h1>update_house</h1>")

def delete_house(request):
    return Httpresponse("<h1>delete_house</h1>")