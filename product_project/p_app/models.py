from django.db import models

# Create your models here.

class ProductModel(models.Model):
    #Fruits, Grocery, Fashion
    PRODUCT_TYPES=[
        ('fruits','Fruits'),
        ('grocery','Grocery'),
        ('fashion','Fashion')
    ]
    prouduct_name = models.CharField(max_length=150,null=True)
    description = models.TextField(null=True)
    product_date = models.DateField(null=True)
    image = models.ImageField(upload_to='media/product_img', null=True)
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.prouduct_name}-{self.description}'