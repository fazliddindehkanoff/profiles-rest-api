from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import TestSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from . import permissions
from . import models

class HelloApiView(APIView):
    """Test api view"""
    serializer_class = TestSerializer

    def get(self, request, format=None):
        """Test api function for get"""

        return Response({"message": "My first api with drf"})

    def post(self, request):
        """Getting data from post method and retrieving it with hello """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")

            return Response({"message": f"Hi {first_name} {last_name} welcome"})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object """
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial updating of an object"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """Handling delete method"""
        return Response({"method":"DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """ Test api view set for understanding and learning"""
    serializer_class = TestSerializer

    def list(self, request):
        """Return Hello world message"""
        return Response({"message":"Hello world this is api created by viewset "})

    def create(self, request):
        """Handle Creating object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")

            return Response({"message": f"Hi {first_name} {last_name} welcome"})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Get object by specific id"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Update part of object"""
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """Delete object by it's Id """
        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle CRUD operations for user profile"""
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.UpdateOwnProfile, AllowAny]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handle CRUD operations for profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Self the profile user to the logged in user"""
        serializer.save(user_profile=self.request.user)
