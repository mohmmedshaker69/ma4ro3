
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Attribute)
# admin.site.register(Attribute_value)
# admin.site.register(StockControl)
# admin.site.register(Image)
# admin.site.register(Inventory)
from django.contrib import admin
from .models import Category, Product, Attribute, AttributeValue, Inventory, StockControl, Image

admin.site.register(Product)

class ProductImageInline(admin.TabularInline):
    model = Image

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue

class StockControlInline(admin.TabularInline):
    model = StockControl

@admin.register(Inventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, StockControlInline]

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
