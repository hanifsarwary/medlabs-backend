"""ambProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from djangoapps.users.api.v1.views import UserTokenObtainPairView


schema_view = get_schema_view(
   openapi.Info(
      title="Amb Poyect API",
      default_version='v1',
      description="A Q-project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # API doc urls
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # admin urls
    url(r'^admin/', admin.site.urls),

    # jwt token urls
    url(r'^api/token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # djangoapps urls
    url(r'^api/', include('djangoapps.urls')),
]
