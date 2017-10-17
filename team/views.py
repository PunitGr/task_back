from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MemberSerializer
from .models import Member


class MemberView(APIView):

    def get_object(self, kwargs):
        member = Member.objects.filter(**kwargs)
        if not member:
            raise Http404
        return member

    def get(self, request):
        """
        Returns all the team members
        """
        kwargs = {}
        userId = request.GET.get("user")
        email = request.GET.get("email")

        if userId is not None and userId != '':
            kwargs["id"] = int(userId)

        if email is not None and email != '':
            kwargs["email"] = email

        if len(kwargs):
            member = self.get_object(kwargs)

        else:
            try:
                member = Member.objects.all()
            except Member.DoesNotExist:
                return Response(
                    {
                        "status": "failed",
                        "results": "No Team members"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

        serializer = MemberSerializer(member, many=True)

        if member:
            return Response(
                {
                    "status": "success",
                    "results": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "status": "failed",
                "results": ""
            },
            status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request):
        """
        To add a team member
        """
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "results": "Successfully created a team member"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "status": "failed",
                "errors": serializer.errors,
                "results": ""
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        kwargs = {}
        userId = request.GET.get("user")
        email = request.GET.get("email")

        if userId is not None and userId != '':
            kwargs["id"] = int(userId)

        if email is not None and email != '':
            kwargs["email"] = email

        if len(kwargs):
            member = self.get_object(kwargs)

            if member:
                member.delete()
                return Response(
                    {
                        "status": "success",
                        "results": "Successfully deleted a team member"
                    },
                    status=status.HTTP_200_OK
                )

        return Response(
            {
                "status": "failed",
                "results": "Matching query not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )


class EditMemberView(APIView):
    def get_object(self, user_id):
        try:
            member = Member.objects.get(id=user_id)
        except Member.DoesNotExist:
            raise Http404
        return member

    def patch(self, request, user_id):
        member = self.get_object(user_id)
        serializer = MemberSerializer(member, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "results": serializer.validated_data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "failed",
                "errors": serializer.errors,
                "results": ""
            },
            status=status.HTTP_201_CREATED
        )
