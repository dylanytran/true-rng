from django.urls import path
from .views import gen_rand

urlpatterns = [
    path('random/<int:min>/<int:max>/', gen_rand, name='gen_rand'),
]