from django.urls import path
from template_app import views

app_name = 'template_app'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]