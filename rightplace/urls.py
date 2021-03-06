"""rightplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from accounts.views import show_index, signup, my_profile

from billing.views import add_credit_card, re_subscribe, subscribe, unsubscribe

from opportunities import urls as opportunities_urls

from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", show_index, name="show_index"),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/profile/", my_profile, name="my_profile"),
    
    path('billing/add_credit_card/', add_credit_card, name='add_credit_card'),
    path('billing/re_subscribe/', re_subscribe, name='re_subscribe'),
    path('billing/subscribe/', subscribe, name='subscribe'),
    path('billing/unsubscribe/', unsubscribe, name='unsubscribe'),
    
    path("posts/", include(opportunities_urls)),
    
    path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
]
