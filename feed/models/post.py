from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Profile

# Create your models here.


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    post_description = models.TextField(default='', null=True, blank=True)
    post_img = models.TextField(default='', null=True, blank=True)
    user_id = models.ForeignKey(
        Profile,
        # Define que, ao excluir o User, todos os posts associados a ele também serão excluídos.
        on_delete=models.CASCADE,
        # Permite que você acesse todos os posts de um usuário usando user.posts.all().
        related_name='post'
    )
