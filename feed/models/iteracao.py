from django.db import models
from feed.models import Post
from cadastro.models import Profile


class Iteracao(models.Model):
    iteracao_id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(
        Profile,
        # Define que, ao excluir o Profile, todos as iteraçoes associados a ele também serão excluídos.
        on_delete=models.CASCADE,
        # Permite que você acesse todos as Iteraçoes de um usuário usando profile.iteracao.all().
        related_name='iteracao'
    )

    post_id = models.ForeignKey(
        Post,
        # Define que, ao excluir o Post, todos as iteraçoes associados a ele também serão excluídos.
        on_delete=models.CASCADE,
        # Permite que você acesse todos as Iteraçoes de um usuário usando post.iteracao.all().
        related_name='iteracao'
    )
    iteracao_comentario = models.TextField()
    iteracao_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comentou: {self.comentario[:30]}..."


class Curtida(models.Model):
    cutida_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='curtidas'
    )
    profile_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='curtidas'
    )
    curtida_criada = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que um Profile só pode curtir um post uma vez
        unique_together = ('post_id', 'profile_id')

    def __str__(self):
        return f"{self.profile_id.id} curtiu {self.post_id.title}"
