from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import MemberSerializer
from .models import Member


class MemberView(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class EditMemberView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return Response(request.data, status=status.HTTP_200_OK)
