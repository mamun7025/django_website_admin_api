from django.urls import path, include
from product_app.api.views import ProductList, ProductKeySpecDel

urlpatterns = [
    path('list/', ProductList.as_view(), name='Product_list'),
    path('productkeyspecdel/', ProductKeySpecDel.as_view(), name='Product_spec_dtl'),
]
