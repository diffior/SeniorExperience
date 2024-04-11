from django.urls import path
from .views import ec2_instance_detail, download_ec2_instance, ec2_instance_list

urlpatterns = [
    path('create/', ec2_instance_list, name='ec2_instance_list'), #create a new EC2 instance
    path('details/<int:pk>/', ec2_instance_detail, name='ec2-detail'), #This show the inputs needed for download/int/
    path('download/<int:pk>/', download_ec2_instance, name='download_ec2_instance'), #this is the url for the download button
]

# path('ec2/<int:pk>/', ec2_instance_detail, name='ec2_instance_detail'),
# path('', ec2_instance_list, name='ec2_instance_list'),
# path('ec2/', list_ec2_instances, name='ec2_instances_list'), #To do: list all ec2 instances
# path('download-yaml/', download_yaml, name='download_yaml'),
# path('ec2/download/<int:pk>/', download_ec2_instance, name='download_ec2_instance'),