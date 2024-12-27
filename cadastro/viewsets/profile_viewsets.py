from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

from ..models import Profile
from ..serializers import ProfileSerializer


class ProfileViewSets(ModelViewSet):
    queryset = Profile.objects.all()  # Definindo o queryset
    serializer_class = ProfileSerializer


class FollowUserView(APIView):
    def post(self, request, user_id):
        # ele busca o usuario que voce quer adicionar pelo user_id
        user_to_follow = get_object_or_404(Profile, pk=user_id)
        # usa o usuario passado pelo request para poder adicionar o usuario
        request.user.profile.profile_connections.add(user_to_follow)
        return Response({'message': f"Voçê agora esta seguindo {user_to_follow.user.username}"})

    def delete(self, request, user_id):
        user_to_unfollow = get_object_or_404(Profile, pk=user_id)
        # pega este objeto que veio no request e remove user_to_unfollow das conneções
        request.user.profile.profile_connections.remove(user_to_unfollow)
        return Response({'message': f"Voçê deu unfollow em {user_to_unfollow.user.username}"})


@api_view(['GET'])
def get_user_profile(request, pkuser):
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(user=pkuser)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# para mostar quem o user esta seguindo


class UserFollowingView(APIView):
    def get(self, request, pkuser):
        try:
            # Pegue o perfil do usuário com base no ID do usuário
            user_profile = Profile.objects.get(user=pkuser)

            # Pegue todas as conexões que o usuário está seguindo
            following_profiles = user_profile.profile_connections.all()

            # Serializa as conexões (perfis seguidos)
            serializer = ProfileSerializer(following_profiles, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'message': 'Perfil não encontrado'}, status=status.HTTP_404_NOT_FOUND)
