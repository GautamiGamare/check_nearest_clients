from django.contrib import admin
from django.urls import path
from app1 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index1.html"),name="main"),
    path('location/',views.location,name='location'),
    path('distance/',views.dist,name="distance"),

    path('new_york/',views.new_york,name='new_york'),
    path('boston/', views.boston, name='boston'),
    path('los_angeles/', views.los_angeles, name='los_angeles'),
    path('chicago/', views.chicago, name='chicago'),
    path('houston/', views.houston, name='houston'),
    path('phoenix/', views.phoenix, name='phoenix'),
    path('san_diego/', views.san_diego, name='san_diego'),
    path('dallas/', views.dallas, name='dallas'),
    path('san_jose/', views.san_jose, name='san_jose'),
    path('austin/', views.austin, name='austin'),
    path('columbus/', views.columbus, name='columbus'),

]
