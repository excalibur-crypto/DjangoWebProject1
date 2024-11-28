"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('about/', views.about, name='about'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Войти',
                 'year' : datetime.now().year,
             }

         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('products/', views.product_list, name='product_list'),  # Добавлено
    path('products/create/', views.product_create, name='product_create'),  # Добавлено
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('anketa/', views.anketa, name='anketa'),
    # path('', include('DjangoWebProject1.urls')),
    path('Link/', views.Link, name='Link'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
