from django.urls import path,include
from .import views


app_name = 'index_page'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),
    path('ruk/', views.ruk.as_view(),name = 'ruk'),
    path('strukt/', views.struct.as_view(),name = 'struct'),
    path('polozh/', views.polozh.as_view(),name = 'polozh'),

]