from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from skills.forms import CustomPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skills.urls')),
    
    # Custom styled password reset view using CustomPasswordResetForm
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm
    ), name='password_reset'),
    
    # Custom login view pointing to your template
    path('accounts/login/', auth_views.LoginView.as_view(template_name='skills/login.html'), name='login'),
    
    # Include all other built-in auth routes (password reset done, confirm, complete, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]