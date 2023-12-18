from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 100,null  = models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
    
class Product (models.Model):
    name = models.CharField(max_length = 200,null = models.CASCADE)
    price = models.PositiveBigIntegerField(null = models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE,null = models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    def __str__(self) :
        return self.name