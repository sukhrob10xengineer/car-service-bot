from django.contrib import admin
from .models import UserModel,Order

class UserModelAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "user_type")
    list_display_links = ("user_id", )


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(Order)

