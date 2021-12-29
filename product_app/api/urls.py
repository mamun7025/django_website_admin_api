from django.urls import path, include
from product_app.api.views import ProductDetails, ProductList, ProductKeySpecDel

urlpatterns = [
    path('list/', ProductList.as_view(), name='Product_list'),
    path('productkeyspecdel/', ProductKeySpecDel.as_view(), name='Product_spec_dtl'),
    # R&D
    path('getAll/', ProductList.getAll),
    path('productDetails/<int:pk>/', ProductList.productDetails),
    path('<int:pk>/', ProductDetails.as_view(), name='Product_Details'),
]
