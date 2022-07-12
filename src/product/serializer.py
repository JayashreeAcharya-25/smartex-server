from dataclasses import field
from rest_framework import serializers
from src.product.models import Product, models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'