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
     path('register/done/', views.AdvUserRegisterDoneView.as_view(),
          name='register_page_done'),
     path('profile/change/', views.AdvUserChangeInfoView.as_view(),
          name='profile_change_page'),
     path('password/change/', views.AdvUserPasswordChangeView.as_view(),
          name='password_change_page'),
     path('profile/', views.profile, name='profile_page'),
     path('profile/all_list_lessons/', views.profile_all_list_lessons,
          name='profile_all_list_lessons_page'),
     path('profile/buy_list_lessons/', views.profile_buy_list_lessons,
          name='profile_buy_list_lessons_page'),
     path('lesson/<int:pk>/', views.lesson_detail,
          name='lesson_detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
