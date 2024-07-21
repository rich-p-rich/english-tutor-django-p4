"""
URL configuration for english_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_accounts/', include('user_accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('appointments/', include("appointments.urls"), name='appointments-urls'), 
    path('homepage/', include("home.urls"), name='home-urls'),
    path('games-and-exercises/', include('games_and_exercises.urls'), name='games_and_exercises.urls'),
    path('', HomePage.as_view(), name='homepage'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
