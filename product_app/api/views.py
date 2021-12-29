from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
from product_app.models import Product, ProductKeySpecs, ProductDetailSpecs, ProductDetailSpecsDtl
from product_app.api.serializers import ProductSerializer, ProductKeySpecsSerializer, ProductDetailSpecsSerializer, ProductDetailSpecsDtlSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # data = list(queryset.values())
    # # data = queryset.values()
    # JsonResponse(data, safe=False)

    def getAll(request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        # data = list(queryset.values())
        # return JsonResponse(serializer_class.data)

    def productDetails(request, pk):
        product = Product.objects.get(pk=pk)
        # serializer_class = ProductSerializer
        data = {
            'movies': product.productCode,
            'name': product.productName,
        }
        return JsonResponse(data)


class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductKeySpecDel(generics.ListAPIView):
    queryset = ProductDetailSpecs.objects.all()
    serializer_class = ProductDetailSpecsSerializer
