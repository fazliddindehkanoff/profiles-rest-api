from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.HelloApiView.as_view(), name="test-api")
]
