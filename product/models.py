from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255, null=True)
    
    def __str__(self):
       return self.name

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    
    def __str__(self):
       return f' {self.title} - {self.category}'
   
class Review(models.Model):
    text=models.TextField(null=True, blank=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='reviews' )
    STARS=(
    (i, '*' * i) for i in range(1, 6)
)
    stars=models.IntegerField(choices=STARS, default=5, null=True)
    @property
    def reviews_name(self):
      return [i.name for i in self.reviews.all()]
    
    def __str__(self):
       return f'{self.product} : {self.text}- {self.stars}'
   
