from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, response, format=None):
        """Returns a list of APIView features"""
        an_apiView = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is a similar to traditional django view'
        ]

        return Response({'message':'Hello','an_apiView':an_apiView})

