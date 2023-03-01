from django.contrib import admin
from .models import *


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    ordering = ('parent', )

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(author=request.user)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'position', 'visible', 'parent']
    inlines = (MenuItemInline, )


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'css_class', 'visible']
    inlines = (MenuItemInline, )



admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
