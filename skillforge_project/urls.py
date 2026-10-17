from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skills.urls')),
    
    # Custom login view pointing to your template
    path('accounts/login/', auth_views.LoginView.as_view(template_name='skills/login.html'), name='login'),
    
    # Include all built-in auth routes (password reset, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]