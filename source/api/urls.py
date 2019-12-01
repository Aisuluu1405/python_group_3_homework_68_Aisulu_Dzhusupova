from django.urls import path
from .views import api_example, add, subtract, multiply, divide

app_name = 'api'

urlpatterns = [
    path('echo/', api_example, name='echo_api'),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),

]

