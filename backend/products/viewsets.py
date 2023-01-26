from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get-> list->queryset
    get-> retrieve-> Product Instance detail view
    post -> crete -> new Instance
    put-> update -> 
    patch->partial update
    delete-> destroy ->existing instance
    """
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    lookup_field = 'pk'