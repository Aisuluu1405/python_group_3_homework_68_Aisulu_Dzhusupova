from django.urls import path
from .views import api_example, add_numbers, subtract_numbers, multiply_numbers, divide_numbers

app_name = 'api'

urlpatterns = [
    path('echo/', api_example, name='echo_api'),
    path('add/', add_numbers, name='add'),
    path('subtract/', subtract_numbers, name='subtract'),
    path('multiply/', multiply_numbers, name='multiply'),
    path('divide/', divide_numbers, name='divide'),

]

