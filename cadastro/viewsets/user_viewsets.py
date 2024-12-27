
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from ..serializers import UserSerializers

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')  # Define o queryset diretamente
    serializer_class = UserSerializers

    def perform_create(self, serializer):

        serializer.save()


@api_view(['GET'])
def get_username(request, nome):
    if request.method == 'GET':
        try:
            isUsername = User.objects.get(username=nome)

            serializer = UserSerializers(isUsername)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
