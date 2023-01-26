from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True) # renaming a property object from the product model
    url = serializers.SerializerMethodField(read_only=True) 
    preferred_url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')

    email =  serializers.EmailField(write_only=True)

    class Meta:
        model =Product
        fields=['preferred_url','url','email','pk','title', 'content','price', 'sale_price','discount'] 
    

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get('title')
    #     return instance

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not  isinstance(obj, Product):
            return None
        return obj.get_discount()