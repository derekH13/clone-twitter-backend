from os.path import basename

from django.urls import path, include
from rest_framework import routers

from .viewsets import FollowUserView, UserFollowingView
from cadastro import viewsets

from cadastro import viewsets

router = routers.SimpleRouter()

router.register(r'cadastro', viewsets.UserViewSet, basename='cadastro')
router.register(r'profile', viewsets.ProfileViewSets, basename='profile-all')

urlpatterns = [
    path('', include(router.urls)),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', FollowUserView.as_view(), name='unfollow-user'),
    path('profileUser/<int:pkuser>/',
         viewsets.get_user_profile, name='profile-user'),
    path('username/<str:nome>/',
         viewsets.get_username, name='get-username'),
    path('profile/<int:pkuser>/following/',
         UserFollowingView.as_view(), name='user-following'),
    # método list() dentro do as_view(), que é o método correspondente a uma requisição GET no ModelViewSet.
]
