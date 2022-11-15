from rest_framework import viewsets
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import F


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'amount', 'time']
    search_fields = ['category']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user.id)

    def create(self, request):
        if request.data['type'] == 'DE':
            request.data['user'] = self.request.user.id
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.request.user.balance = F('balance') - request.data['amount']
            self.request.user.save()
            return Response(serializer.data)

        request.data['user'] = self.request.user.id
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.request.user.balance = F('balance') + request.data['amount']
        self.request.user.save()
        return Response(serializer.data)


