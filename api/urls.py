from xml.etree.ElementInclude import include
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path('shop/', views.Shop, name='shop'),
    path('about/', views.About, name='about'),
    path('service/', views.Service, name='service'),
    path('blog/', views.Blog, name='blog'),
    path('contact/', views.Contact, name='contact'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('confirm/', views.ConfromOrder, name='confirm'),

    path('signin/', views.sign_up, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),

    path('profile/', views.profile, name='profile'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
