from django.urls import path
from blog.views import show_home


urlpatterns = [
    path('',show_home, name = 'home_url'),
]
