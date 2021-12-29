from rest_framework import serializers
from product_app.models import Product, ProductKeySpecs, ProductDetailSpecs, ProductDetailSpecsDtl


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
