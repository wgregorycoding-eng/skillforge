from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from skills.forms import CustomPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skills.urls')),
    
    # Password Reset Overrides
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),
    
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    # Custom login view
    path('accounts/login/', auth_views.LoginView.as_view(template_name='skills/login.html'), name='login'),
    
    # Other built-in auth routes (like logout)
    path('accounts/', include('django.contrib.auth.urls')),
]