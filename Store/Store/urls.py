"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from Store import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from dj_rest_auth.views import PasswordResetConfirmView
from .views import TemplateVerify


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # override the email verification template
    path(
        'api-dj-rest-auth/registration/account-email-verification-sent/', TemplateVerify.as_view(),
        name='account_email_verification_sent',
    ),

    # override name the url
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/v1/', include('products.urls',namespace='api-v1-products')),
    path('api/v1/', include('comments.urls',namespace='api-v1-comments')),
    path('api/v1/', include('galleries.urls',namespace='api-v1-galries')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)