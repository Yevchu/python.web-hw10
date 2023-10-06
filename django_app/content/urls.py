from django.urls import path
from . import views

app_name = 'content'
urlpatterns = [
    path('', views.main, name='main'),
    path('top_tags/', views.top_ten_tag, name='tags'),
    path('add_tags/', views.add_tag, name='add_tags'),
    path('add_quote/', views.add_quote, name='add_quote')
]