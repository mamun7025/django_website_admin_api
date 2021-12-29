from django.contrib import admin
from product_app.models import Product, ProductKeySpecs, ProductDetailSpecs, ProductDetailSpecsDtl

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductKeySpecs)
admin.site.register(ProductDetailSpecs)
admin.site.register(ProductDetailSpecsDtl)
