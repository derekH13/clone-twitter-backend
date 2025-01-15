from django.http import JsonResponse
from rest_framework.views import APIView
from ..models import Curtida, Post, Iteracao

from ..serializers import CurtidaSerializer, IteracaoSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

from cadastro.models import Profile


@api_view(['POST'])
def curtir_post(request, postId, profileId):
    try:
        post = Post.objects.get(post_id=postId)
        profile = Profile.objects.get(id=profileId)
    except:
        return Response({'message': 'Post ou profile não encontrado!'}, status=status.HTTP_404_NOT_FOUND)

    if post.curtidas.filter(profile_id=profile.id).exists():
        return Response({'message': 'profile ja deu like!'}, status=status.HTTP_409_CONFLICT)

    # Criar uma nova curtida
    Curtida.objects.create(post_id=post, profile_id=profile)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def all_curtidas(request, postId):
    try:
        post = Post.objects.get(post_id=postId)
        item = post.curtidas.all()

        serializer = CurtidaSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        # Caso ocorra algum erro, retorna uma resposta com status 500 (erro interno do servidor)
        return Response({'error': str(e)}, status=500)
# PARA COMENTAR


@api_view(['POST'])
def comentar_post(request, postId, profileId):
    post = Post.objects.get(post_id=postId)
    profile = Profile.objects.get(id=profileId)
    comentario = request.POST.get('iteracao_comentario')

    if not comentario:
        return Response({'message': 'Sem comentario'}, status=status.HTTP_401_UNAUTHORIZED)

    Iteracao.objects.create(
        post_id=post, profile_id=profile, iteracao_comentario=comentario)
    return JsonResponse({'message': 'Comentário adicionado com sucesso!'})


@api_view(['GET'])
def all_comentarios(request, postId):
    try:
        post = Post.objects.get(post_id=postId)
        item = post.iteracao.all()

        serializer = IteracaoSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        # Caso ocorra algum erro, retorna uma resposta com status 500 (erro interno do servidor)
        return Response({'error': str(e)}, status=500)
# PARA COMENTAR
