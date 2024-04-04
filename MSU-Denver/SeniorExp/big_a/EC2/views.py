import yaml
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EC2Instance  # Adjust this import to match your model
from .serializers import EC2Serializer  # Adjust this import to match your serializer
from .forms import SaveYAMLForm
from django.shortcuts import render
from .forms import SaveYAMLForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def ec2_instance_list(request):
    """
    List all EC2 instances, or create a new EC2 instance.
    """
    if request.method == 'GET':
        instances = EC2Instance.objects.all()
        serializer = EC2Serializer(instances, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EC2Serializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()  # Save the instance and keep the returned instance
            response_data = {'pk': saved_instance.pk, 'data': serializer.data}  # Include the primary key and serialized data in the response
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ec2_instance_detail(request, pk):
    """
    Retrieve, update, or delete an EC2 instance.
    """
    try:
        instance = EC2Instance.objects.get(pk=pk)
    except EC2Instance.DoesNotExist:
        return Response({'message': 'The EC2 instance you are looking for does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EC2Serializer(instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EC2Serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Update was successful!', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        instance.delete()
        return Response({'message': 'EC2 instance was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
def download_yaml(request):
    if request.method == 'POST':
        form = SaveYAMLForm(request.POST)
        if form.is_valid():
            # Process the form and return a downloadable YAML response
            # (see previous instructions for generating and returning the YAML file)
            pass  # Placeholder for your YAML generation and response logic
    else:
        form = SaveYAMLForm()

    # Specify the path to your template:
    # Adjust 'EC2/download_form.html' if your app or template is named differently
    return render(request, 'EC2/download_form.html', {'form': form})

api_view(['GET'])
def download_ec2_instance(request, pk):
    # Get the EC2Instance object or return a 404 if not found
    instance = get_object_or_404(EC2Instance, pk=pk)
    
    # Generate the YAML configuration using the to_ansible_playbook method
    yaml_content = instance.to_ansible_playbook()
    
    # Create an HttpResponse object with the YAML content
    response = HttpResponse(yaml_content, content_type="application/x-yaml")
    # Set the Content-Disposition header to prompt a download
    response['Content-Disposition'] = f'attachment; filename="ec2_instance_{pk}.yaml"'
    
    return response

