from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=['user']

    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('Price value must be greater than 0')
        return value
    
    def update(self, instance, validated_data):
        request = self.context['request']
        user = request.user

        # Prevent non-admins from changing price
        if 'price' in validated_data:
            if not (
                user.role == 'admin' or 
                user.is_staff or 
                user.is_superuser
            ):
                validated_data.pop('price')

        return super().update(instance, validated_data)

            



