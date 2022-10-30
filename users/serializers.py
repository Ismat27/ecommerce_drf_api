from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

class UserRegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'password1'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError({'passwords':'passwords do not match'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password1 = validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
    


