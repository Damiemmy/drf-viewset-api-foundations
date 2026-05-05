from rest_framework import serializers
from .models import Product,Listing

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
                # raise serializers.ValidationError('price cannot be changed after a booking has been made')
                raise serializers.ValidationError('Price cannot be change after approval from admin')

        return super().update(instance, validated_data)

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields="__all__"

    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("price value must be greater than zero")
        return value

            



