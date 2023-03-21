from django.contrib import admin
from .models import User,Contact,Product,Wishlist,Cart,Transaction
# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Transaction)