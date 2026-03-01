from django.urls import path
from . import utils
urlpatterns = [
    path('build/<int:id>', utils.build, name = 'build'),
]