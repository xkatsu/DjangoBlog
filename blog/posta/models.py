from django.db import models
from django.db.models.deletion import DO_NOTHING
from categorias.models import Categoria
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(
        User, on_delete=DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(
        upload_to='post_img', verbose_name='Imagem')  # /%Y/%m/%d -> dps do post_img
    publicado_post = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post
