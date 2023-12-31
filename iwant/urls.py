"""iwant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from safety_wear import views
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("",include("iwish.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("safety/",include('safety_wear.urls')),
    path("api/",include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('', page_not_found, name='404'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
