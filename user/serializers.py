from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(max_length=128,
                                     style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email',
                  'is_staff', 'user_photo', 'password']
        extra_kwargs = {
            'url': {
                'lookup_field': 'username'
            }
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserFrontendSerializer(serializers.ModelSerializer):

    user_photo = serializers.ImageField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_staff',
                  'user_photo', 'password']

    # used to make sure the user submitted
    # password is hashed when the user is created.
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class ConsumerFrontEndSerializer(serializers.ModelSerializer):

    user_photo = serializers.ImageField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_staff',
                  'user_photo', 'password']

    # used to make sure the user submitted
    # password is hashed when the user is created.
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserRetrieveSerializer(serializers.ModelSerializer):

    user_photo = serializers.ImageField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_photo']