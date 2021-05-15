from django.urls import path
from .import views

app_name = 'reports'
urlpatterns = [
    path('', views.IndexPageView.as_view(),name = 'index'),
    path('reports_one/', views.reports_one.as_view(),name = 'reports_one'),
    path('rep_template/', views.rep_template.as_view(),name = 'rep_template'),
    path('reports_two/', views.reports_two.as_view(),name = 'reports_two'),
    path('reports_three/', views.reports_three.as_view(),name = 'reports_three'),
    path('reports_four/', views.reports_four.as_view(),name = 'reports_four'),
]