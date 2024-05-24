from django.urls import path
from django.urls import register_converter
from .views import gen_rand
from .converters import NegativeIntConverter

register_converter(NegativeIntConverter, 'negint')

urlpatterns = [
    path('random/<negint:min>/<negint:max>/', gen_rand, name='gen_rand'),
]