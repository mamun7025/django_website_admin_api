from rest_framework import serializers
from product_app.models import Product, ProductKeySpecs, ProductDetailSpecs, ProductDetailSpecsDtl


class ProductDetailSpecsDtlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetailSpecsDtl
        # fields = "__all__"
        exclude = ('status', 'creator', 'createdAt',
                   'lastUpdateBy', 'lastUpdatedTime',)
        # depth = 1


class ProductDetailSpecsSerializer(serializers.ModelSerializer):
    details = ProductDetailSpecsDtlSerializer(many=True, read_only=True)

    class Meta:
        model = ProductDetailSpecs
        # fields = "__all__"
        exclude = ('status', 'creator', 'createdAt',
                   'lastUpdateBy', 'lastUpdatedTime',)


class ProductKeySpecsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductKeySpecs
        # fields = "__all__"
        exclude = ('status', 'creator', 'createdAt',
                   'lastUpdateBy', 'lastUpdatedTime',)


class ProductSerializer(serializers.ModelSerializer):
    keySpechs = ProductKeySpecsSerializer(many=True, read_only=True)
    spechDetails = ProductDetailSpecsSerializer(many=True, read_only=True)

    class Meta:

        model = Product
        # fields = "__all__"
        exclude = ('status', 'creator', 'createdAt',
                   'lastUpdateBy', 'lastUpdatedTime',)
