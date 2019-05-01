from django.urls import path
from .import views


from django.contrib import admin
from django.urls import path, include
#from users import views as user_views
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.views.static import serve

from django.conf.urls import include, url
from django.conf.urls.static import static

from rest_framework import routers

router = routers.DefaultRouter()
router.register('productsAPI', views.ProductView)


app_name = "Eshop"

urlpatterns = [
    path('', views.home, name= 'home'),
    path('adminCustom/', views.adminCustom, name= 'adminCustom'),
    path('adminCustom2/', views.adminCustom2, name= 'adminCustom2'),
    path('createProduct/', views.createProduct, name= 'createProduct'),
    path('allProducts/', views.allProducts, name= 'allProducts'),

    path('login/', auth_views.LoginView.as_view(template_name='Eshop/login.html'), name= 'login'),
    path('logout/', views.logout_request, name= 'logout'),
    path('register/', views.register, name= 'register'),



   path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='Eshop/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='Eshop/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='Eshop/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='Eshop/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('product/<int:id>/', views.productDetailPage, name= 'product'),

    path('cart/', views.cart, name= 'cart'),
   # path('cart/<slug:product>/', views.add_to_cart, name= 'update_cart'),
    path('cart/<int:id>/', views.add_to_cart, name='update_cart'),
    path('cartDelete/<int:id>/', views.deleteFromCard, name='cartDelete'),
    path('Order/<int:id>/', views.order, name='order'),

    path('emailView/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),

    #path('api/', views.ProductView),
    path('', include(router.urls))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
