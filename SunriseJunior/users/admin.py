from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'email', 'is_active')
    list_display_links = ('id', 'email')
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    search_fields = ()
    readonly_fields = []
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'first_name',
                'last_name',
            ),
        }),
    )