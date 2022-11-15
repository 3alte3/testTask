from rest_framework import viewsets
from registration.models import NewUser
from registration.serializers import ProfileSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
import requests


class Profile(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        tempResponse = requests.get('http://127.0.0.1:8000/auth/users/me/',
                                    headers={'Authorization': f'{request.headers["Authorization"]}'}).json()
        queryset = NewUser.objects.get(id=tempResponse['id'])
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return Response(status=404, data={'message': 'Not found'})
