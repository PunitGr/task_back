import urllib
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from .models import Member


def reverse_with_urlparams(path, **kwargs):
    return path + '?' + urllib.parse.urlencode(kwargs)


class MemberTestCase(APITestCase):
    """
    Test Case to check MemberView
    """

    def create_member(self, userId, email):
        url = reverse("users")
        data = {
            "userId": userId,
            "email": email,
            "firstName": "Test",
            "lastName": "Last",
            "phoneNumber": "+919911139678",
            "role": 0
        }

        return self.client.post(url, data, headers={"Content-Type": "application/json"})

    def test_post(self):
        response = self.create_member(1, "test@example.com")
        self.assertEqual(201, response.status_code)

    def test_get_no_members(self):
        url = reverse("users")
        response = self.client.get(url, headers={"Content-Type": "application/json"})
        self.assertEqual(404, response.status_code)

    def test_get(self):
        self.create_member(2, "test123@example.com")
        url = reverse("users")

        # To check all the team members
        response = self.client.get(url, headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)

        # check a specific team member
        url = reverse_with_urlparams(reverse("users"), user=2)
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        self.create_member(3, "test1234@example.com")
        url = reverse_with_urlparams(reverse("users"), user=3)

        # To check all the team members
        response = self.client.delete(url, headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)


class EditMemberTestCase(APITestCase):
    """
    Test Case for Editting member details
    """
    def create_member(self, userId, email):
        url = reverse("users")
        data = {
            "userId": userId,
            "email": email,
            "firstName": "Test",
            "lastName": "Last",
            "phoneNumber": "+919911139678",
            "role": 0
        }

        self.client.post(url, data, headers={"Content-Type": "application/json"})

    def test_patch(self):
        self.create_member(4, "test12345@example.com")
        url = reverse("edit", kwargs={"user_id": 4})
        data = {
            "firstName": "Tester"
        }
        response = self.client.patch(url, data, headers={"Content-Type": "application/json"})
        self.assertEqual(201, response.status_code)
        self.assertEqual("Successfully updated info", response.data["results"])
