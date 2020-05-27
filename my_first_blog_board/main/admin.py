from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from . import models


class LessonsInlineAdmin(admin.TabularInline):
    model = models.AdvUser.lessons.through

@admin.register(models.AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_activated', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions'),
        }),
        (_('Other info'), {'fields': ('send_message',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login', 'date_joined')
    inlines = (LessonsInlineAdmin,)
    form = UserChangeForm

    def lookup_allowed(self, lookup, value):
        # Don't allow lookups involving passwords.
        return not lookup.startswith(
            'password') and super().lookup_allowed(lookup, value)


class FollowersInlineAdmin(admin.TabularInline):
    model = models.Lesson.followers.through


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title',)}),
        (_('Personal info'), {'fields': ('author',)}),
        (_('Important dates'), {'fields': ('created', 'update', 'published')}),
    )
    inlines = (FollowersInlineAdmin,)
    readonly_fields = ('update',)
    list_display = ('id', 'title', 'author', 'created', 'update', 'published')
    search_fields = ('title', 'author')

    class Meta:
        model = models.Lesson


@admin.register(models.LesonTube)
class LesonTubeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title',)}),
        (_('Personal info'), {'fields': ('author',)}),
        (_('Important dates'), {'fields': ('created',)}),
    )
    readonly_fields = ('created',)
    list_display = ('id', 'title', 'author', 'created')
    search_fields = ('title', 'author')

    class Meta:
        model = models.LesonTube


# admin.site.register(models.AdvUser, AdvUserAdmin)
