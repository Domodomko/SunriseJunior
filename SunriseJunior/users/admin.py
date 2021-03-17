from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)


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