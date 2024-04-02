from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['instance_name', 'host_ip', 'user', 'ssh_key_path', 'python_interpreter']



