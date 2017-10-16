from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_role(self, obj):
        role = obj.role
        if role == "R":
            return "Regular"
        else:
            return "Admin"
