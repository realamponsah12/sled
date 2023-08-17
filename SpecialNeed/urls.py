"""
URL configuration for SpecialNeed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views as BV
from django.conf.urls.static import static
from SpecialNeed import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",BV.index,name='index' ),
    path("contact",BV.contact, name='contact'),
    path('upload/', BV.image_upload_view, name='upload'),
    path('about/', BV.about, name='about'),
    path('blog/<int:blog_id>', BV.display_blog, name='display_blog'),
    path('donate', BV.donate, name='donate'),
    path('add_comment', BV.add_comment, name='add_comment'),
    path('permission', BV.permission, name='permission'),
    path('contact_us', BV.contact_m, name='contact_us'),
    path('newsletter', BV.newsletter, name='newsletter'),
    path('donate_m', BV.donate_m, name='donate_m'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
