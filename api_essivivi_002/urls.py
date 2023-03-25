"""api_essivivi_002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from essivivi_api.views import * 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('essivivi_api.urls')),
    # path('api/auth/auth-token', obtain_auth_token, name= 'obtain_auth_token')
    path('api/register/', RegisterView.as_view(), name= 'register'),
    path('api/register/agent/', RegisterAgentView.as_view(), name= 'register'),
    path('api/auth/login/', LoginView.as_view(), name= 'login'),
    path('api/login/', TokenObtainPairView.as_view(), name= 'login'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name= 'refreshToken'),
]


urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)