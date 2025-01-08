from rest_framework import serializers
from ..models import Curtida, Iteracao


class IteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Iteracao
        fields = [
            'iteracao_id', 'profile_id', 'post_id', 'iteracao_comentario', 'iteracao_criada'
        ]


class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Curtida
        fields = [
            'cutida_id', 'profile_id', 'post_id', 'curtida_criada'
        ]
