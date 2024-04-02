from rest_framework import serializers
from .models import EC2Instance


class EC2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EC2Instance
        fields = '__all__'


