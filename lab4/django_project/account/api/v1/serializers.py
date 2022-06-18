from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True},
            # 'password_confirm': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "password Didn't Match"}
            )
        else:

            user.set_password(self.validated_data.get('password'))
            user.save()
            return user
