from rest_framework import serializers
from src.brands.models import Brands

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
