# urls.py
from django.urls import include, path
from . import views
from django.contrib import admin

app_name = 'inventory'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/', views.inventory_detail, name='inventory-detail'), #Retrieve Inventory file with pk/id
    path('', views.inventory_list, name='inventory-list'), # Shows all inventory files and creates
    path('download/<int:pk>/', views.download_inventory, name='download_inventory'), #Also grabs inventory file with pk/id and able to download
]

