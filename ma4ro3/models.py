from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')  

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
   
    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, related_name='attribute_values', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    attribute_values = models.ManyToManyField(AttributeValue) 
    
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 
    sku = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.product.name
    
class StockControl(models.Model):
    last_checked = models.DateTimeField(auto_now=True)  
    units = models.IntegerField(default=0)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)

class Image(models.Model):
    url = models.ImageField(upload_to='product_images/')  
    alternative_text = models.CharField(max_length=50)
    is_feature = models.BooleanField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='images') 

    def __str__(self):
        return f"Image for {self.inventory.product.name}"
