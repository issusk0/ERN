from django.urls import path
from . import views
urlpatterns = [
    path('build/<int:id>', views.build, name = 'build'),
]