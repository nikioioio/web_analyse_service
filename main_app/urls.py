from django.urls import path,include
from .import views


app_name = 'index_page'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),

]