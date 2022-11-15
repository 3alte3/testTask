from rest_framework import serializers
from statistic.models import UserStatistic


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistic
        fields = '__all__'
