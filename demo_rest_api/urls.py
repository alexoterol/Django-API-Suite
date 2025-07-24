from django.urls import path
from . import views

urlpatterns = [
   path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources" ),
   
   # Ruta que recibe un ID como parámetro y usa la vista DemoRestApiItem
    path("<str:id>/", views.DemoRestApiItem.as_view(), name="demo_rest_api_item"),
]