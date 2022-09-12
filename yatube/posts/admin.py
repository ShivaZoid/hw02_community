from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    """Конфигурация отображения данных.

    Attributes:
        list_display: отображаемые поля.
        list_editable: изменение поле group в любом посте.
        search_fields: интерфейс для поиска по тексту постов.
        list_filter: возможность фильтрации по дате.
        empty_value_display: «пусто» становится ссылкой, для перехода на
                             страницу редактирования поста.
    """

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
