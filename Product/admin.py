from django.contrib import admin
from .models import CategoryModel,ProductModel,BrandModel
# Register your models here.


class SlugFieldAddBrand(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand",)}

class SlugFieldAddCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}


admin.site.register(CategoryModel,SlugFieldAddCategory)
admin.site.register(BrandModel,SlugFieldAddBrand)
admin.site.register(ProductModel)
