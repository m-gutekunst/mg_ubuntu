from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='mainpage'),
    path('unauthorized_access/', views.unauthorized_access,
         name='unauthorized_access'),
]
