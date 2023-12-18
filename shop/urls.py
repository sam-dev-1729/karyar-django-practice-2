from django.urls import path

from .views import product_details, product_list

app_name = "shop"
urlpatterns = [
    path("", product_list, name="list"),
    path("<int:pk>/", product_details, name="detail"),
]
