# urls.py
from django.urls import include, path
from . import views
from django.contrib import admin

app_name = 'inventory'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventory/', views.inventory_list, name='inventory-list'),
    path('/<int:pk>/', views.inventory_detail, name='inventory-detail'), #Retrieve Inventory file with pk/id
    path('', views.inventory_list, name='inventory-list'), # Shows all inventory files
    path('download/<int:pk>/', views.download_inventory, name='download_inventory'),
]

