from django.urls import path
from webapp.views.calculator import add, subtract, multiply, divide


urlpatterns = [
    path("add/", add),
    path("subtract/", subtract),
    path("multiply/", multiply),
    path("divide/", divide),
]
