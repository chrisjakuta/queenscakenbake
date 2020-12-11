from rest_framework import serializers
from .models import (
    LandingPageModel,
    LandingPageCollectDataModel,
)

class LandingPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LandingPageModel
        fields = [
            'name',
            'header_text',
            'image',
            'landing_page_text',
            'product_section_header_text',
            'product_section_text',
        ]

class LandingPageCollectDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = LandingPageCollectDataModel
        fields = [
            'id',
            'name',
            'full_name',
            'email',
            'user_message',
        ]