from django.urls import path
from .import views

app_name = 'upr'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),

]