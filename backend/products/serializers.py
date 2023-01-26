from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True) # renaming a property object from the product model
    class Meta:
        model =Product
        fields=['pk','title', 'content','price', 'sale_price','discount'] 
    
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not  isinstance(obj, Product):
            return None
        return obj.get_discount()