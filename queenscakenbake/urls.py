"""queenscakenbake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from user.views import (UserModelView, CustomUserModelViewSet)
from products.views import (
    Confectionery,
    ConfectioneryDetail,
)
from content.views import (
    LandingPageView,
    LandingPageCollectDataView,
    index,
)
from rest_framework.authtoken import views
# for single page application
# index = never_cache(TemplateView.as_view(template_name='build/index.html'))
admin.site.site_header = 'Queens Cake N Bake 🎂 Admin'
admin.site.site_title = 'Data Management Admin Portal'
admin.site.index_title = 'Welcome to the Queens admin portal.'

react_url_patterns = [
    path('', index, name='index'),
    path('home/', index, name='index'),
    path('login/', index, name='index'),
    path('confectionery/', index, name='index'),
    path('confectionery/<str:type>/', index, name='index'),
    path('confectionery/<str:type>/<str:name>', index, name='index'),
    path('<slug:username>/', index, name='index'),
]

api_endpoint_patterns = []

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('authtoken/', views.obtain_auth_token),
    path('salesman/', include('salesman.urls')),
    path('landing/', LandingPageView.as_view()),
    path('contact/', LandingPageCollectDataView.as_view()),
    path('product/', Confectionery.as_view({'get':'list'})),
    path('product/<str:type>', Confectionery.as_view({'get':'list'})),
    path('product/<str:type>/<str:name>', ConfectioneryDetail.as_view()),
    path('user/<slug:username>/', UserModelView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include(react_url_patterns)),
]
