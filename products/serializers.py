from rest_framework import serializers
from .models import (
    CakeModel,
    CupcakesModel,
    ParfaitModel,
    PieModel,
    Products,
)

class CupcakesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'photo_description',
            'price',
            'quantity',
        ]
class CakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'photo_description',
            'price',
            'quantity',
        ]

class ParfaitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'photo_description',
            'price',
            'quantity',
        ]

class PieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'photo_description',
            'price',
            'quantity',
        ]

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'type',
            'name',
            'description',
            'photo_description',
            'price',
            'quantity',
        ]
