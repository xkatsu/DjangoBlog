from django.db import models
from django.db.models.deletion import DO_NOTHING
from posta.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentarios(models.Model):
    nome_comentario = models.CharField(max_length=200)
    email_comentario = models.EmailField(verbose_name='email')
    comentario = models.TextField(verbose_name='comentario')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(
        User, on_delete=DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicacao_comentario = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_comentario
