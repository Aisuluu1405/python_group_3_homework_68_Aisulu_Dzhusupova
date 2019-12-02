from django.urls import path
from .views import index

app_name = 'webapp'

urlpatterns = [
    path('', index, name='index_page'),

]