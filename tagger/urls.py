"""tagger URL Configuration

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
from django.conf.urls import url, include
from django.views.generic import TemplateView
from front_tag.views import NormaList #2
from django.urls import reverse

#url(r'^django-sb-admin/', include('django_sb_admin.urls')),
#url(r'^accounts/login/$', auth_views.login,{'template_name': 'django_sb_admin/examples/login.html'}),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^front_tag/', include('front_tag.urls')),
    #path('norma/', TemplateView.as_view(template_name = "norma/list_norma.html")),
    #path('norma/' , NormaList.as_view(), name='list'),   # 2
    url(r'^django-sb-admin/', include('django_sb_admin.urls')),
    #path(r'accounts/login/$', auth_views.login,{'template_name': 'django_sb_admin/examples/login.html'}),
]
