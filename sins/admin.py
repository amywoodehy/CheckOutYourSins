from django.contrib import admin

# Register your models here.
from sins.models import Sin, Sinner


@admin.register(Sin)
class SinAdmin(admin.ModelAdmin):
    pass


@admin.register(Sinner)
class SinnerAdmin(admin.ModelAdmin):
    pass
