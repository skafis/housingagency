from django.shortcuts import render, get_object_or_404, redirect
from .models import Houses
from .forms import add_houseForm

# Create your views here.
def home_page(request):
    view = Houses.objects.order_by('-timestamp')
    context = {
        'view': view
    }
    return render(request, 'agency/index.html', context)

def add_house(request):
    form = add_houseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
    	instance = form.save(commit=False)
        print form.cleaned_data.get('name') 
    	instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render (request, 'agency/new_post.html', {'form': form})

def house_detail(request, pk):
    view = get_object_or_404(Houses, pk=pk)
    context = {
        'view' : view
    }
    return render(request, 'agency/house_detail.html', context)

def update_house(request, pk=None):
    instance = get_object_or_404(Houses, pk=pk)
    form = add_houseForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        
    context = {
        'view': instance,
        'form' : form,
    }
    return render(request, 'agency/new_post.html', context)
def delete_house(request, pk=None):
    instance = get_object_or_404(Houses, pk=pk)
    instance.delete()
    return redirect ('index.html')