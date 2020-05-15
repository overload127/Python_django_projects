from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.urls import path
# from django.conf.urls import url
from django.views.decorators.cache import never_cache

from .views import BBLoginView, BBLogoutView, index, other_page, profile
from .views import BBPasswordChangeView, ChangeUserInfoForm
from .views import BBPasswordResetCompleteView
from .views import BBPasswordResetConfirmView, BBPasswordResetDoneView
from .views import BBPasswordResetView, DeleteUserView
from .views import RegisterDoneView, RegisterUserView, user_activate
from .views import profile_bb_detail, by_rubric, detail
from .views import profile_bb_add, profile_bb_delete, profile_bb_change


app_name = 'main'
urlpatterns = [
     path('accounts/password_reset/',
          BBPasswordResetView.as_view(
               template_name='main/password_reset_request.html',
               subject_template_name='email/password_subject_request.txt',
               email_template_name='email/password_reset_request.txt'),
          name='password_reset_request'),
     path('accounts/password_reset/done/', BBPasswordResetDoneView.as_view(
          template_name='main/password_reset_done.html'),
          name='password_reset_done'),
     path('accounts/password_rreset/confirm/<uidb64>/<token>/',
          BBPasswordResetConfirmView.as_view(
               template_name='main/password_reset_confirm.html'),
          name='password_reset_confirm'),
     path('accounts/password_reset/complete/',
          BBPasswordResetCompleteView.as_view(
               template_name='main/password_reset_complete.html'),
          name='password_reset_complete'),
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
     path('accounts/profile/<int:pk>', profile_bb_detail,
          name='profile_bb_detail'),
     path('accounts/profile/change/<int:pk>/', profile_bb_change,
          name='profile_bb_change'),
     path('accounts/profile/delete/<int:pk>/', profile_bb_delete,
          name='profile_bb_delete'),
     path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
     path('accounts/profile/', profile, name='profile'),
     path('accounts/login/', BBLoginView.as_view(), name='login'),
     path('accounts/profile/delete/', DeleteUserView.as_view(),
          name='profile_delete'),
     path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
     path('', index, name='index'),
     path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
     path('<int:pk>/', by_rubric, name='by_rubric'),
     path('<str:page>/', other_page, name='other'),
]


if settings.DEBUG:
    urlpatterns.append(path('static/<path:path',
                            never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
