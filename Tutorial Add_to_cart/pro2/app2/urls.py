from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.home,name='home'),
   path('productview/<int:pk>/',views.productview,name='productview'),
    path('signup',views.signup_user,name='signup_user'),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logoutuser,name='logout_user'),

   #  cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
   #  till here
  
]

if (settings.DEBUG):
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)