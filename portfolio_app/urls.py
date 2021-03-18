from django.contrib import admin
from django.urls import path, include
from portfolio_app import views

# Django admin header customization
admin.site.site_header = "Omega's Portfolio"
admin.site.site_title = "Welcome to Omega's dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
