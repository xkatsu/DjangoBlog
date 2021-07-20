from django.contrib import admin
from .models import Comentarios


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario', 'post_comentario',
                    'data_comentario', 'publicacao_comentario')
    list_editable = ('post_comentario',)

    list_display_links = ('id', 'nome_comentario', 'email_comentario', )


admin.site.register(Comentarios, ComentariosAdmin)
