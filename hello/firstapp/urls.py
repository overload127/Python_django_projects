from django.urls import path, re_path
from django.views.generic import TemplateView

from firstapp import views


app_name = 'first_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('index2/', views.index2, name='home2'),
    path('index3/', views.index3, name='index3'),
    path('create/', views.create, name='create'),
    path('edit/<int:_id>/', views.edit, name='edit'),
    path('delete/<int:_id>/', views.delete, name='delete'),
    re_path(r'^about', TemplateView.as_view(
        template_name='firstapp/about.html',
        extra_context={'header': 'О сайте'}),
            name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    path('details/', views.details, name='details'),
    re_path(r'^products/', views.products, name='products_null'),
    re_path(r'^products/(?P<productid>\d+)/', views.products, name='products'),
    re_path(r'^users/(?P<_id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    path('adv_products/', views.products),
    path('adv_products/<int:productid>/', views.products),
    path('adv_users/', views.users),
    path('adv_users/<int:_id>/<name>/', views.users),
    path('board/<int:boardid>/', views.board),
    path('cases/', views.cases),
    path('m304/', views.m304),
    path('m400/', views.m400),
    path('m403/', views.m403),
    path('m404/', views.m404),
    path('m405/', views.m405),
    path('m410/', views.m410),
    path('m500/', views.m500),
    path('fun/<int:count>/', views.fun, name='fun'),
    path('fun2/<int:count>/', views.fun2, name='fun2'),
]
