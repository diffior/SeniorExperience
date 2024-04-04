from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Inventory
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def inventory_list(request):
    """
    List all inventory items, or create a new inventory item.
    """
    if request.method == 'GET':
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            saved_instance = serializer.save()  # Save the instance and keep the returned instance
            response_data = saved_instance.pk  # Add the pk to the response data
            serializer = InventorySerializer(saved_instance)  # Re-serialize the instance to include the pk
            response_data = {'pk': saved_instance.pk, 'data': serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk):
    """
    Retrieve, update, or delete an inventory item.
    """
    try:
        item = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return HttpResponse({'message': 'Inventory you are looking for does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Update was  successful!'}, serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response({'message': 'Inventory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def download_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    
    # Generate the INI content using the to_ini method
    ini_content = inventory.to_ini()
    
    # Create an HttpResponse object with the INI content
    response = HttpResponse(ini_content, content_type="text/plain")
    # Set the Content-Disposition header to prompt a download
    response['Content-Disposition'] = f'attachment; filename="inventory_{pk}.ini"'
    
    return response


