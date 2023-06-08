from django.contrib import admin

from .models import Values

# Register your models here.


class ValuesAdmin(admin.ModelAdmin):
    list_display = ("id", "valueList")


admin.site.register(Values, ValuesAdmin)
