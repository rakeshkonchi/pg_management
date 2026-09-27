"""
URL configuration for pg_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from adminapp.views import login,dashboard,adminprofile,adminprofileupdate,addRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/',login, name='admin_login_link'),
    path('admin_dashboard/', dashboard, name = 'admin_dashboard_link'),
    path('admin_profile/',adminprofile,name='admin_profile_link'),
    path('admin_profile_update/',adminprofileupdate,name='admin_profile_update_link'),
    path('add_room/', addRoom, name='add_room_link')
]
if settings.DEBUG:

    urlpatterns = urlpatterns+static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)