from django.urls import path
from django.contrib.auth.views import LogoutView 

from users import views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('login/', views.MyLoginView.as_view(),name='login'),
    # The next_page argument specifies the URL that the users will be redirected to once they log out successfully.
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', views.RegisterView.as_view(),name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]
