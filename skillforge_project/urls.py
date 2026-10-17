from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from skills.forms import CustomPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skills.urls')),
    
    
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        template_name='skills/registration/password_reset_form.html'
    ), name='password_reset'),
    
    # Custom login view
    path('accounts/login/', auth_views.LoginView.as_view(template_name='skills/login.html'), name='login'),
    
    # All other auth routes
    path('accounts/', include('django.contrib.auth.urls')),
]