from django.urls import path
from .import views

app_name = 'obuch'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),
    path('calendar/', views.calendar.as_view(),name = 'calendar'),
    path('present/', views.present.as_view(),name = 'present'),

]