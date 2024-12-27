from django.http import HttpResponse, JsonResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer

from django.contrib.auth.models import User
from cadastro.models import Profile


class PostViewSets(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('post_id')


@api_view(['GET'])
def user_all_post(request, pkuser):
    if request.method == 'GET':
        try:
            user = Profile.objects.get(pk=pkuser)
            todos_posts = user.post.all()

            serializer = PostSerializer(todos_posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
