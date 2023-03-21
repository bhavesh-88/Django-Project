from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to='profile_pic/',default='')
	usertype=models.CharField(max_length=100,default='buyer')

	def __str__(self):
		return self.fname


class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		#return self.id
		return str(self.id)+'-'+self.name


class Product(models.Model):
	category=(
			('men','men'),
			('women','women'),
			('kid','kid'),
		)
	size=(
			('S','S'),
			('M','M'),
			('L','L'),
			('XL','XL'),
			('XXL','XXL'),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=category)
	product_name=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_desc=models.CharField(max_length=100)
	product_size=models.CharField(max_length=100,choices=size)
	product_image=models.ImageField(upload_to="product_pic/")

	def __str__(self):
		return self.seller.fname+"-"+self.product_category


class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+' - '+self.product.product_name


class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_price=models.PositiveIntegerField()
	product_qty=models.PositiveIntegerField()
	total_price=models.PositiveIntegerField()
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+' - '+self.product.product_name

# <---paytm integration --->

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

# <---end--->







