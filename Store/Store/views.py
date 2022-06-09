import imp
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)


    def delete(self,request):
        request.auth.delete()
        return Response()