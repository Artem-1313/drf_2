from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['name', 'description', 'rate', 'status', 'owner']
        read_only_fields = ['owner', 'status']



