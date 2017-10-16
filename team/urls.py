from django.conf.urls import url
from .views import MemberView, EditMemberView

urlpatterns = [
    url(r'^$', MemberView.as_view(), name="users"),
    url(r'^edit/(?P<user_id>[0-9]+)/$', EditMemberView().as_view(), name="edit")
]
