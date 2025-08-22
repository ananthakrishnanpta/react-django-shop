from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, obj):
        request = self.context.get('request')
        if obj.picture:
            return request.build_absolute_uri(obj.picture.url)
        return None

    class Meta:
        model = Product
        fields = '__all__'
