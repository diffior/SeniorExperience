from django.urls import path
from .views import ec2_instance_list, ec2_instance_detail, download_yaml, download_ec2_instance

urlpatterns = [
    path('ec2/', ec2_instance_list, name='ec2_instance_list'),
    path('ec2/<int:pk>/', ec2_instance_detail, name='ec2_instance_detail'),
    path('', ec2_instance_list, name='ec2_instance_list'),
    path('<int:pk>/', ec2_instance_detail, name='inventory-detail'),
    path('download-yaml/', download_yaml, name='download_yaml'),
    path('ec2/download/<int:pk>/', download_ec2_instance, name='download_ec2_instance'),
]
