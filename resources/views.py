from django.shortcuts import render, redirect
from .models import Resource
from .forms import ResourceForm

def filter_resources(request):
    categories = request.GET.getlist('category')
    if categories:
        resources = Resource.objects.filter(category__in=categories)
    else:
        resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})


def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
        
    else:
        form = ResourceForm()
    return render(request, 'resources/add_resource.html', {'form': form})