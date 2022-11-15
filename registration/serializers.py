from rest_framework import serializers
from registration.models import NewUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields =('id','user_name','first_name','second_name','balance')
