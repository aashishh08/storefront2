from rest_framework import serializers
from .models import Product, Collection, Review
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count'] 

    products_count = serializers.IntegerField(read_only= True)


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     collection = serializers.HyperlinkedRelatedField(
#         queryset = Collection.objects.all(),
#         view_name = 'collection-detail'
#     )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory','unit_price', 'price_with_tax', 'collection']
                        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.2)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
    


