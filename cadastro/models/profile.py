from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

# symmetrical=False: significa que a relação não precisa ser recíproca (ex.: o usuário A segue B, mas B não necessariamente segue A).


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)

    profile_connections = models.ManyToManyField(
        'self',
        # Se for verdadeiro, seguir alguém significa que essa pessoa também te segue
        symmetrical=False,
        related_name='followers',  # Nome inverso para os seguidores
        blank=True  # Permite que o usuário comece sem seguir ninguém
    )

    def __str__(self):
        return self.user.username

# O sinal post_save é disparado automaticamente sempre que um objeto do modelo User é salvo.


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
