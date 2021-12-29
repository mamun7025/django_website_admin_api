from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework import generics
from product_app.models import Product, ProductKeySpecs, ProductDetailSpecs, ProductDetailSpecsDtl
from product_app.api.serializers import ProductSerializer, ProductKeySpecsSerializer, ProductDetailSpecsSerializer, ProductDetailSpecsDtlSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductKeySpecDel(generics.ListAPIView):
    queryset = ProductDetailSpecs.objects.all()
    serializer_class = ProductDetailSpecsSerializer
