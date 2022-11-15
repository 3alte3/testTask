from rest_framework import generics
from rest_framework.response import Response
from transaction.models import Transaction
from statistic.models import UserStatistic
from statistic.serializers import StatisticSerializer
from django.db.models import Max, Min, Sum
from category.models import Category


class Statistics(generics.ListAPIView):
    serializer_class = StatisticSerializer

    @staticmethod
    def create_message(minStat, maxStat, minForGroup, sumForAll):
        result = f'Amount of minimal transaction is {minStat["amount__min"]}. Amount of maximum ' \
                 f'transaction is {maxStat["amount__max"]}.For each group total : '
        for x in minForGroup:
            result += str(Category.objects.get(pk=x['category']).name) + f" {x['sum_price']} "
        result += f'. Total: {sumForAll["amount__sum"]}'
        return result

    def get_queryset(self):
        return UserStatistic.objects.all().filter(user=self.request.user.id)

    def get(self, request, *args, **kwargs):
        minStat = Transaction.objects.all().filter(user=self.request.user.id).aggregate(Min('amount'))
        maxStat = Transaction.objects.all().filter(user=self.request.user.id).aggregate(Max('amount'))
        forEach = Transaction.objects.all().filter(user=self.request.user.id).values('category'). \
            annotate(sum_price=Sum('amount'))
        sumForAll = Transaction.objects.all().filter(user=self.request.user.id). \
            aggregate(Sum('amount'))
        return Response(data=Statistics.create_message(minStat, maxStat, forEach, sumForAll))
