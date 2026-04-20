from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= "__all__"
        read_only_fields = ['user']

    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("Price value must be greater than 0")
        return value