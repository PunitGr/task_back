from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("userId", "firstName", "lastName", "phoneNumber", "email", "role")
    list_filter = ["userId"]
    search_fields = ["firstName", "lastName"]


admin.site.register(Member, MemberAdmin)
