from django.urls import path
from . import views
from django.views.generic import TemplateView
from api.views import lost_detail as api_lost_detail

urlpatterns = [
    path("", views.index, name="home"),
    path('report-lost/', views.report_lost, name='report_lost'),
    path('report-found/', views.report_found, name='report_found'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("lost/<int:id>/", api_lost_detail, name="lost_detail"),
    path("found/<int:id>/", views.found_detail, name="found_detail"),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path("login/", views.login_view, name="login"),
    path('signup/', views.signup_page, name='signup'),
    path("my-reports/", views.my_reports, name="my_reports"),
    

]
