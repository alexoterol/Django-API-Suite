from django.urls import include, path
from .views import LandingAPI

urlpatterns = [
    path('index/', LandingAPI.as_view(), name='landing_api_index'),
    path('', LandingAPI.as_view(), name='landing_api_index'),

]
