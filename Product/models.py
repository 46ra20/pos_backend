from django.db import models
from Account.models import User

# Create your models here.
class CategoryModel(models.Model):
    category=models.CharField(max_length=30)
    slug=models.CharField(auto_created=category,max_length=30)

    def __str__(self) -> str:
        return self.category
    

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='./Image/Product')
    price = models.DecimalField(decimal_places=3,max_digits=12)
    quantity = models.IntegerField()
    weight = models.DecimalField(decimal_places=3,max_digits=12)

    category = models.ManyToManyField(CategoryModel)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} by {self.added_by.first_name} {self.added_by.first_name}'