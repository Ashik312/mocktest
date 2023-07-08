from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login1,name='login'),
    path('signup/',views.signup1,name='signup'),
    path('prodetails/<int:pk>',views.prodetails,name='prodetails'),
    path('cart/',views.cart,name='cart'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
