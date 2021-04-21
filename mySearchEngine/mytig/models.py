from django.db import models

# Create your models here.
class ProduitEnPromotion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')
    
    class Meta:
        ordering = ('tigID',)

class ProduitAvailable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)

class ProduitCoquillages(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)
    
class Produit(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')
    name = models.CharField(max_length=2000)
    price = models.FloatField(default = 0.0)
    discount_price = models.FloatField(default = 0.0)
    discount_percent = models.FloatField(default = 0.0)
    quantity = models.IntegerField(default = 0)
    sales_number = models.IntegerField(default = 0)
    comments = models.CharField(max_length=2000)
    category = models.IntegerField(default='-1')

class Transaction(models.Model):
    date = models.CharField(max_length=2000)
    price = models.FloatField(default = 0.0)
    quantity = models.IntegerField(default='0')
    tigID = models.IntegerField(default='-1')
    transaction_type = models.IntegerField(default='-1')
