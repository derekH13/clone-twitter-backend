from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            # garante que a senha não sera exibida
            'password': {'write_only': True}
        }
    # Quando você tenta criar ou atualizar um usuário, o método validate_email será chamado automaticamente.

    # verificando se o email ja existe
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email já está em uso.')
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Criptografa a senha
        user.save()
        return user
