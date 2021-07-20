from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('titulo_post', 'autor_post', 'data_post',
                    'categoria_post', 'publicado_post')

    list_editable = ('publicado_post',)

    list_editable_links = ('id', 'titulo_post',)

    summernote_fields = ('conteudo_post',)


admin.site.register(models.Post, PostAdmin)
