from django.contrib import admin
from .models import Joint


@admin.register(Joint)
class JointAdmin(admin.ModelAdmin):
    #list_editable   = ['application']
    list_filter     = ['created_at', 'updated_at',]
    search_fields   = ['name', 'description']
    list_display    = ['name', 'is_active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fields          = ['name', 'description', 'is_active', 'created_at', 'updated_at']
    #登録時にオートコンプリートで探せる
    #autocomplete_fields = ['application']

