from django.urls import path
from post_page import views

app_name = 'post_page'

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
]