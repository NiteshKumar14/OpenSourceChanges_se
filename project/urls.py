"""project URL Configuration

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
from django.urls import path, include,reverse_lazy
from natter.views import signup
from private_chat.views import dashboard
from django.conf.urls import include, url
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('natter.urls', namespace='natter')),
    path('undercover/', include('private_chat.urls', namespace='private_chat')),
    path('accounts/signup',signup,name='signup'),
    # path('logout/',auth_views.logout_then_login,name='logout'),
    path("accounts-dashboard", dashboard, name="dashboard"),
    path('accounts/',include('django.contrib.auth.urls')),
    url('',include('social_django.urls',namespace='social')),
   ]