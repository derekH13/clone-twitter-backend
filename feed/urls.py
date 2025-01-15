from os.path import basename

from django.urls import path, include
from rest_framework import routers

from feed import viewsets

router = routers.SimpleRouter()
# registrando as rotas e as viewsets
router.register(r'post', viewsets.PostViewSets, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('postUser/<int:pkuser>/', viewsets.user_all_post, name='post-user'),
    path('postComentar/<int:postId>/<int:profileId>/',
         viewsets.comentar_post, name='comentrar'),
    path('postComentarios/<int:postId>/',
         viewsets.all_comentarios, name='comentrarios'),
    path('postCurtir/<int:postId>/<int:profileId>/',
         viewsets.curtir_post, name='curtir'),
    path('postCurtidas/<int:postId>/', viewsets.all_curtidas, name='curtidas')

]
