from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Test api function for get"""
        
        return Response({"message": "My first api with drf"})
