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
]
