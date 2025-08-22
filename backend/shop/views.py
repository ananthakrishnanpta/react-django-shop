from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    
class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id = product_id)
        serializer = ProductSerializer(product, many = False, context = {'request': request})
        return Response(serializer.data)