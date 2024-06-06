from django.shortcuts import render, redirect
from .models import Resource
from .forms import ResourceForm

def resource_list(request):
    resources = Resource.objects.all()

    category = request.GET.getlist('category')
    resource_location = request.GET.getlist('location')

    if category:
        resources = resources.filter(category__in=category)
    if resource_location:
        resources = resources.filter(location__in=resource_location)
    
    context = {
        'resources': resources,
        'categories': Resource.objects.values_list('category', flat=True).distinct(),
        'locations': Resource.objects.values_list('location', flat=True).distinct(),
    }

    return render(request, 'resources/resource_list.html', context)

def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
        
    else:
        form = ResourceForm()
    return render(request, 'resources/add_resource.html', {'form': form})