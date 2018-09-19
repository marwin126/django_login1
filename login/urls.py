"""django_login1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path
# from login import views
#
# urlpatterns = [
#     path(r'^register', views.register),
#     path(r'^login', views.login),
# ]

# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^', include('login.urls')),
# ]

from django.conf.urls import url
from login import views
urlpatterns = [
    url(r'^$', views.register),
    url(r'^register$',views.register),
    #url(r'^register_success$',views.register_success),
    url(r'^registerDB$',views.registerDB),
    url(r'^login$',views.login),
    url(r'^login_check$',views.login_check),
    #url(r'^(\d+)$',views.detail),
]