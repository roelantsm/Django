from django.db import models
from django.utils.timezone import now
# Create your models here.
#from .utils import unique_order_id_generator

class Category(models.Model):
    soort = models.CharField(max_length=200)
          
    def __str__(self):
        return self.soort

    def publish(self):
        self.save()

class Adress(models.Model):
    straat = models.CharField(max_length=200)
    nr = models.CharField(max_length=200)
    stad  = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    land = models.CharField(max_length=200)
            
    def __str__(self):
        return self.straat





class Product(models.Model):
    naam =  models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    prijs = models.DecimalField(decimal_places=2, max_digits=100)
    btw  = models.DecimalField(decimal_places=2, max_digits=100)
    merk = models.CharField(max_length=201)
    image = models.ImageField(upload_to='images/')   
    productCount = models.IntegerField(default=3)
    korting = models.DecimalField(decimal_places=2, max_digits=100, default =0)
    timestamp = models.DateField(default=now, blank=True)

    def __str__(self):
        return self.naam

    def publish(self):
        self.save()

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem, null = True, blank=True)
    #products = models.ManyToManyField(Product, null = True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default = True)
    
    def __unicode__(self):
        return "Cart id: %s"(self.id)

    def publish(self):
        self.save()
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null = True, blank=True, on_delete=models.PROTECT)

    product = models.ForeignKey(Product, null = True, blank=True, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    line_toal = models.DecimalField(default = 10.99, max_digits=100, decimal_places=2)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        try:
            return str(self.cart.id)
        except: 
             return self.product.title

status = (
        ('created', 'created'),
        ('paid', 'paid'),
        ('shipped', 'shipped'),
        ('refunded', 'refunded'),
    )
    

class Order(models.Model):
    order_id = models.CharField(max_length=150, blank=True)
    billingAdress =  models.ForeignKey(Adress, on_delete=models.PROTECT,blank=True, null=True)
    #shippingAdress =  models.ForeignKey(Adress, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default="created", choices=status)
    shipping_total = models.DecimalField( default = 0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id
    def publish(self):
        self.save()