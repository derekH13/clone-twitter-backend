from django.http import JsonResponse
from ..models import Curtida, Post, Iteracao


def curtir_post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    profile = request.profile_id

    if post.curtidas.filter(profile_id=profile).exists():
        return JsonResponse({'message': 'Você já curtiu este post!'}, status=400)

    Curtida.objects.create(post_id=post, post_id=profile)
    return JsonResponse({'message': 'Post curtido com sucesso!'})


# PARA COMENTAR
def comentar_post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    profile = request.profile_id
    comentario = request.POST.get('iteracao_comentario')

    if not comentario:
        return JsonResponse({'message': 'Comentário não pode estar vazio!'}, status=400)

    Iteracao.objects.create(
        post_id=post, profile_id=profile, iteracao_comentario=comentario)
    return JsonResponse({'message': 'Comentário adicionado com sucesso!'})
