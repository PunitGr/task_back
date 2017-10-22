from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "phoneNumber", "email", "role")
    list_filter = ["email"]
    search_fields = ["firstName", "lastName"]


admin.site.register(Member, MemberAdmin)
