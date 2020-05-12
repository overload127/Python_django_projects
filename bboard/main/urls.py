from django.urls import path

from .views import BBLoginView, BBLogoutView, index, other_page, profile
from .views import BBPasswordChangeView, ChangeUserInfoForm
from .views import RegisterDoneView, RegisterUserView, user_activate

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(),
         name='register'),
    path('accounts/profile/change/', ChangeUserInfoForm.as_view(),
         name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
