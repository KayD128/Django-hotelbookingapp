"""hotelbooking URL Configuration

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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from hotelbooking.staffapp.views import SignUpView
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('staff/', TemplateView.as_view(template_name='for_staff.html'), name='staff'),
    re_path(r'^pictures', TemplateView.as_view(template_name='pictures.html'), name='pictures'),
    re_path(r'^rooms', TemplateView.as_view(template_name='rooms.html'), name='rooms'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name= "signup"),
    re_path(r'^staff/', include('hotelbooking.staffapp.urls')),
    re_path(r'^bookingapp/', include('hotelbooking.bookingapp.urls')),
    re_path(r'^customer/', include('hotelbooking.customerapp.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
