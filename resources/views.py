from django.shortcuts import render
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all()

    category = request.GET.get('category')
    resource_location = request.GET.get('location')

    if category:
        resources = resources.filter(category=category)
    if resource_location:
        resources = resources.filter(location=resource_location)

    context = {
        'resources': resources,
        'categories': Resource.objects.values_list('category', flat=True).distinct(),
        'location': Resource.objects.values_list('location', flat=True).distinct(),
    }

    return render(request, 'resources/resource_list.html', context)

