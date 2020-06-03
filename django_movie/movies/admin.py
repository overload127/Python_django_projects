from django.contrib import admin
from django.utils.html import mark_safe
from django import forms

from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Категории"""
    list_display = ['id', 'name', 'url']
    list_display_links = ['name']


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = 'Изображение'


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    """Фильмы"""
    list_display = ['title', 'category', 'url', 'draft']
    list_filter = ['category', 'year']
    search_fields = ['title', 'category__name']
    inlines = [MovieShotsInLine, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ['draft']
    readonly_fields = ['get_image']
    form = MovieAdminForm
    actions = ['published', 'unpublished']
    fieldsets = [
        (None, {
            'fields': [('title', 'tagline')]
        }),
        (None, {
            'fields': ['description', ('poster', 'get_image')]
        }),
        (None, {
            'fields': [('year', 'world_premier', 'country')]
        }),
        ('Actors', {
            'classes': ['collapse'],
            'fields': [('actors', 'directors', 'genres', 'category')]
        }),
        (None, {
            'fields': [('budget', 'fees_in_usa', 'fees_in_world')]
        }),
        ('Options', {
            'fields': [('url', 'draft')]
        }),
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110">')

    get_image.short_description = 'Постер'

    def unpublished(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def published(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    published.short_description = 'Опубликовать'
    published.allowed_permissions = ['change']

    unpublished.short_description = 'Снять с публикации'
    unpublished.allowed_permissions = ['change']


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ['name', 'email', 'parent', 'movie', 'id']
    readonly_fields = ['name', 'email']


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    """Жанры"""
    list_display = ['name', 'url']


@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    """Актеры"""
    list_display = ['name', 'age', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Изображение'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ['star', 'movie', 'ip']


@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    """Кадры из фильма"""
    list_display = ['title', 'movie', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Изображение'


admin.site.register(RatingStar)

admin.site.site_title = 'django Movies'
admin.site.site_header = 'django Movies'
