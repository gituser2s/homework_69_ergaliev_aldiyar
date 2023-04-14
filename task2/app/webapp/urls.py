from django.urls import path
from webapp.views.calculator import add, IndexView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/", add, name="add"),
]
