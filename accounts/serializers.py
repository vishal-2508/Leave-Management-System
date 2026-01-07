from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'first_name', 'last_name' ]

    def create_user(self, user_data_dict):
        user = User.objects.create_user(
            username=user_data_dict['username'],
            password=user_data_dict['password'],
            first_name=user_data_dict.get('first_name'),
            last_name=user_data_dict.get('last_name'),
            user_type=user_data_dict.get('user_type'),
            email=user_data_dict.get('email')
        )
        return user

