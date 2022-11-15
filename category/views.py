from rest_framework import viewsets
from category.models import Category
from category.serializers import CategorySerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CreateCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'user']
    search_fields = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset()).filter(name=kwargs['name'])
        instance.delete()
        print(kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT,data='ok')
