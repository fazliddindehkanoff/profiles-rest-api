from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TestSerializer

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

        
