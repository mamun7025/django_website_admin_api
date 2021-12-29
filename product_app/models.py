from django.db import models

# Create your models here.


class Product(models.Model):
    productCode = models.CharField(max_length=20)
    productName = models.CharField(max_length=50)
    descrition = models.TextField(blank=True, max_length=250)
    productLogo = models.CharField(max_length=500, blank=True)
    productLogoAlt = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    creator = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdateBy = models.CharField(max_length=20)
    lastUpdatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName


class ProductKeySpecs(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=500)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="keySpechs")
    status = models.BooleanField(default=True)
    creator = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdateBy = models.CharField(max_length=20)
    lastUpdatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductDetailSpecs(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=500)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="spechDetails")
    status = models.BooleanField(default=True)
    creator = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdateBy = models.CharField(max_length=20)
    lastUpdatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductDetailSpecsDtl(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=500)
    ProductDetailSpecs = models.ForeignKey(
        ProductDetailSpecs, on_delete=models.CASCADE, related_name="details")
    status = models.BooleanField(default=True)
    creator = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdateBy = models.CharField(max_length=20)
    lastUpdatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
