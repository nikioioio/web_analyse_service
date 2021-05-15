from django.urls import path
from .import views

app_name = 'infocentr'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),
    path('pl_mer/', views.pl_mer.as_view(),name = 'pl_mer'),
    path('ism/', views.ism.as_view(),name = 'ism'),
    path('ism/docs', views.ism_doc.as_view(),name = 'ism_doc'),
    path('ism/card_process', views.card_process.as_view(),name = 'card_process'),
]