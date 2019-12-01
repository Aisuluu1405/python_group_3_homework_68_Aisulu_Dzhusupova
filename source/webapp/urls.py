from django.urls import path
from .views import

app_name = 'webapp'

urlpatterns = [
    path('index/', index, name='index_page'),

]