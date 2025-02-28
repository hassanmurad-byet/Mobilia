from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('DHAKA', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Khulna','Khulna'),
    ('Rajshahi','Rajshahi'),
    ('Barisal','Barisal'),
    ('Sylhet','Sylhet'),
    ('Rangpur','Mymensingh'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(choices=STATE_CHOICES, max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = [
    ('C', 'Chier'),
    ('T', 'Table'),
    ('S', 'Sofa'),
    ('CR', 'Craft'),

]
STOCK_CHOICES = [
    ('IN STOCK', 'IN STOCK'),
    ('SOLD OUT', 'SOLD OUT'),

]

class Product(models.Model):
    title = models.CharField(max_length=100)
    spec = models.TextField()
    selling_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    availability = models.CharField(choices=STOCK_CHOICES, max_length=50,default='IN_STOCK')
    product_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id) 
    
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price
    

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed','Packed'),
    ('On The Way', 'On The Way'),
    ('Delivery completed', 'Delivery completed'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_note = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')


    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price

