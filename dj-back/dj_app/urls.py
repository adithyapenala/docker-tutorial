"""
URL configuration for dj_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dj_web_app import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("book/", views.create_booking, name="create_booking"),
]

if getattr(settings, 'ENABLE_GRAPHQL', False):
    urlpatterns += [
        path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]
else:
    urlpatterns += [
        path("book/", views.create_booking, name="create_booking"),
        # path("book/<int: pk>", views.get_bookings, name="get_bookings"),
    ]