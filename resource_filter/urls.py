
from django.contrib import admin
from django.urls import path
from resources import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('add/', views.add_resource, name='add_resource'),
    path('admin/', admin.site.urls),
]
