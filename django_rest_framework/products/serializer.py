
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    def validate_price(self, value):  #for prise
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value   
    
    def validate_name(self, value): # for name
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty.")
        return value