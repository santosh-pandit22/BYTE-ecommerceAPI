from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    isbn=models.CharField(max_length=15)
    price=models.FloatField()
    stock=models.IntegerField()
    description=models.TextField()
    written_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True)
    class Meta:
        ordering=['-written_date']
        
    def __str__(self):
            return self.name

class Product(models.Model):
    product_tag=models.CharField(max_length=100) 
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price=models.FloatField()
    stock=models.IntegerField()
    created_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)



