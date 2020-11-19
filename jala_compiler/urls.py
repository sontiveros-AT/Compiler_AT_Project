"""jala_compiler URL Configuration

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
# new lines gonzalo.alarcon
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
# no name line
from django.urls import path, include
from code_editor.views import custom_views

urlpatterns = [
    path('', custom_views.home),
    path('admin/', admin.site.urls),
    path('api/v1/', include('code_editor.urls')),
]

# Add a new PATH to set a default folder
if settings.DEBUG:
    urlpatterns += [
        url(r'^storage/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
