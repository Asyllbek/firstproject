from django.urls import path
from mysite.views import index, generic


urlpatterns = [
    path('', index, name='index'),
    path('generic/', generic, name='generic'),
]

