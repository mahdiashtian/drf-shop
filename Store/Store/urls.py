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
from django.urls import path , include , re_path
from Store import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .views import TemplateVerify
from rest_framework_simplejwt import views as jwt_views
from dj_rest_auth.views import PasswordResetConfirmView , UserDetailsView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Store API",
      default_version='v1',
      description="End point description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ovverride the user view
    path('user/', UserDetailsView.as_view(), name='user_details'),

    # override the email verification template
    path(
        'api-dj-rest-auth/registration/account-email-verification-sent/', TemplateVerify.as_view(),
        name='account_email_verification_sent',
    ),

    # override name the url
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('api-dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/', include('comments.urls',namespace='api-v1-comments')),
    path('api/', include('products.urls',namespace='api-v1-products')),
    path('api/', include('galleries.urls',namespace='api-v1-galries')),
    path('api/', include('categorys.urls',namespace='api-v1-category')),
    path('api/', include('orders.urls',namespace='api-v1-orders')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('__debug__/', include('debug_toolbar.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)