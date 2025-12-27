from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from inventory.models import Inventory

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        product = serializer.save()
        Inventory.objects.create(product=product)