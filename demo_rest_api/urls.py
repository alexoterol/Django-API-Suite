from django.urls import path
from .views import DemoRestApi, DemoRestApiItem
from . import views

urlpatterns = [
   path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources" ),

   # Ruta que recibe un ID como parámetro y usa la vista DemoRestApiItem
   # ESTA ES LA CLAVE
   path("<str:id>/", DemoRestApiItem.as_view(), name="demo_rest_api_item"),
]