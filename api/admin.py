
from django.contrib import admin
from .models import(Customer, Product,Cart,OrderPlaced)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','address', 'city','zipcode','email','phone']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','description','spec', 'category','availability','product_image']




@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']



@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product' ,'quantity','ordered_date','status']
