from django.contrib import admin

from .models import (
    NoteBook,
    Label,
    Note,
)


class NoteBookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
    )
    search_fields = (
        'title',
        'description',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )


class LabelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
    )
    search_fields = (
        'title',
        'description',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'note',
        'notebook',
    )
    filter_horizontal = (
        'labels',
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
        'notebook',
        'labels',
    )
    search_fields = (
        'title',
        'note',
    )
    raw_id_fields = (
        'notebook',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )


admin.site.register(NoteBook, NoteBookAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Note, NoteAdmin)
