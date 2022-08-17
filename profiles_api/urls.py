from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("test-viewset", views.HelloViewSet, basename="test-viewset")
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    path("test/", views.HelloApiView.as_view(), name="test-api"),
    path("", include(router.urls))
]
