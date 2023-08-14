from django.urls import path
from . import views

urlpatterns = [
        path('',views.login_page,name='login'),
        path('signup',views.register,name='signup'),
        path('logout',views.logout,name='logout'),
        path('store/', views.store, name="store"),
        path('cart/', views.cart, name="cart"),
        path('checkout/', views.checkout, name="checkout"),
        path('update_item/', views.updateItem, name="update_item"),
        path('process_order/', views.processOrder, name="process_order"),

]