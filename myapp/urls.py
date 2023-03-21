from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('cart/',views.cart,name='cart'),
    path('detail/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('new-password/',views.new_password,name="new-password"),
    path('profile/',views.profile,name='profile'),
    path('seller-index/',views.seller_index,name="seller-index"),
    path('seller-contact/',views.seller_contact,name='seller-contact'),
    path('seller-change-password/',views.seller_change_password,name='seller-change-password'),
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-detail/<int:pk>/',views.seller_product_detail,name='seller-product-detail'),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name='seller-edit-product'),
    path('seller-delete-product/<int:pk>/',views.seller_delete_product,name='seller-delete-product'),
    path('product-detail/<int:pk>/',views.detail,name='product-detail'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name='remove-from-cart'),
    path('change-qty/',views.change_qty,name='change-qty'),
    path('search/',views.search,name='search'),
    path('products500/',views.products500,name='products500'),
    path('products1000/',views.products1000,name='products1000'),
    path('products1500/',views.products1500,name='products1500'),
    path('products2000/',views.products2000,name='products2000'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('myorder/',views.myorder,name='myorder'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),

]
