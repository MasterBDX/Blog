# accounts.passwords.urls.py
 
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.passwords.views import MyPasswordResetView

urlpatterns  = [

 # password settings
    path('password/change/', 
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/passwords/password_change_form.html'
        ), 
        name='password_change'),
    
        path('password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/passwords/password_change_done.html'
        ), 
        name='password_change_done'),

        path('password/reset/', 
        MyPasswordResetView.as_view(template_name='accounts/passwords/password_reset_form.html'), 
        name='password_reset'),

        path('password/reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/passwords/password_reset_done.html'), 
        name='password_reset_done'),
        path('password/reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/passwords/password_reset_confirm.html'), 
        name='password_reset_confirm'),

        path('password/reset/complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/passwords/password_reset_complete.html'), 
        name='password_reset_complete'),
]