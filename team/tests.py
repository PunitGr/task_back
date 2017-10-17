from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class MemberTestCase(APITestCase):
    """
    Test Case to check MemberView
    """

    def create_member(self, email):
        url = reverse("users")
        data = {
            "email": email,
            "firstName": "Test",
            "lastName": "Last",
            "phoneNumber": "+919911139678",
            "role": "R"
        }

        return self.client.post(url, data, headers={"Content-Type": "application/json"})

    def test_post(self):
        response = self.create_member("test@example.com")
        self.assertTrue(status.is_success(response.status_code))

    def test_get_no_members(self):
        url = reverse("users")
        response = self.client.get(url, headers={"Content-Type": "application/json"})
        self.assertTrue(status.is_success(response.status_code))

    def test_get_all_members(self):
        self.create_member("test123@example.com")
        url = reverse("users")

        # To check all the team members
        response = self.client.get(url, headers={"Content-Type": "application/json"})
        self.assertTrue(status.is_success(response.status_code))


class EditMemberTestCase(APITestCase):
    """
    Test Case for Editting member details
    """
    def create_member(self, email):
        url = reverse("users")
        data = {
            "email": email,
            "firstName": "Test",
            "lastName": "Last",
            "phoneNumber": "+919911139678",
            "role": "R"
        }

        response = self.client.post(url, data, headers={"Content-Type": "application/json"})
        return response.data

    def test_get_member(self):
        data = self.create_member("test112345@example.com")
        id = data["id"]

        url = reverse("edit", kwargs={"pk": id})
        response = self.client.get(url, headers={"Content-Type": "application/json"})
        self.assertTrue(status.is_success(response.status_code))

    def test_patch(self):
        data = self.create_member("test12345@example.com")
        id = data["id"]

        url = reverse("edit", kwargs={"pk": id})
        data = {
            "firstName": "Tester"
        }
        response = self.client.patch(url, data, headers={"Content-Type": "application/json"})
        self.assertTrue(status.is_success(response.status_code))

    def test_delete(self):
        data = self.create_member("test1234@example.com")
        id = data["id"]
        url = reverse("edit", kwargs={"pk": id})

        # To check all the team members
        response = self.client.delete(url, headers={"Content-Type": "application/json"})
        self.assertTrue(status.is_success(response.status_code))
