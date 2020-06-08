from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserInformation

# Register your models here.
# admin.site.register(Account, UserAdmin)

class FullUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Account, FullUserAdmin)
admin.site.register(UserInformation)