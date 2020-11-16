"""tkd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('announcements/', views.announcements, name="announcements"),
    path('about/', views.about, name="about"),
    path('events/calendar', views.events_calendar, name="events-calendar"), 
    path('events/list', views.events_list, name="events-list"),
    path('events/past', views.events_past, name="events-past"),
    path('form/<int:id>/',views.forms, name="form"),
    path('gallery', views.gallery, name="gallery"),
    path('gallery/photo/<int:id>', views.gallery_photo, name="photo"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)