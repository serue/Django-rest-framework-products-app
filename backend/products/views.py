from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content=title

        serializer.save(content=content)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET', 'POST'])
def  product_alt_view(request, pk=None, *args, **kwargs):
    if request.method =='GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk)
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)
    if request.method =='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content=title

            serializer.save(content=content)

            return Response(serializer.data)
        return Response({"error":"Invalid data"}, status=400) 


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perfom_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)