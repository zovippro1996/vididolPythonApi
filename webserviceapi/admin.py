from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserInformation, FanRequest, Star

# Register your models here.
# admin.site.register(Account, UserAdmin)

class FullUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(FanRequest)
admin.site.register(Account)
admin.site.register(Star, FullUserAdmin)
