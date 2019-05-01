from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
        'naam', 
        'prijs', 
        'btw', 
        'merk', 
        'image', 
        'productCount', 
        'korting',
        'timestamp')