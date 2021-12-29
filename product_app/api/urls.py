from django.urls import path, include
from product_app.api.views import ProductList

urlpatterns = [
    path('list/', ProductList.as_view(), name='Product_list'),
]
