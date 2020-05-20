from django.urls import path
from my_first_blog_board import settings
from django.conf.urls.static import static

from main import views


app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.AdvUserLoginView.as_view(), name='login_page'),
    path('logout/', views.AdvUserLogoutView.as_view(), name='logout_page'),
    path('register/', views.AdvUserRegisterView.as_view(),
         name='register_page'),
    path('profile/edit/', views.AdvUserChangeInfoView.as_view(),
         name='edit_page'),
    path('profile/', views.profile, name='profile_page'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
