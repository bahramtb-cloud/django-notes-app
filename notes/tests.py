


from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

    def test_note_creation(self):
        note = Note.objects.create(
            title="Test title",
            text="Test text",
            user=self.user,
        )

        self.assertEqual(
            note.title,
            "Test title",
        )

        self.assertEqual(
            note.user,
            self.user,
        )

        self.assertFalse(note.done)
        self.assertFalse(note.favorite)

    def test_user_cannot_delete_another_users_note(self):
        other_user = User.objects.create_user(
            username="otheruser",
            password="OtherPassword123!",
        )

        note = Note.objects.create(
            title="Private note",
            text="This note belongs to another user",
            user=other_user,
        )

        self.client.force_login(self.user)

        response = self.client.post(
            reverse("delete_note", args=[note.id])
        )

        self.assertEqual(response.status_code, 404)

        self.assertTrue(
            Note.objects.filter(id=note.id).exists()
        )





class NotesAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="api_user",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="other_api_user",
            password="OtherPassword123!",
        )

        self.note = Note.objects.create(
            title="My first note",
            text="This is my first note.",
            user=self.user,
        )

        self.other_note = Note.objects.create(
            title="Private note",
            text="This belongs to another user.",
            user=self.other_user,
        )

        self.list_url = reverse("notes_api")

        self.detail_url = reverse(
            "note_detail_api",
            args=[self.note.id],
        )

        self.other_note_url = reverse(
            "note_detail_api",
            args=[self.other_note.id],
        )

    def test_authenticated_user_can_get_notes(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.get(
            self.list_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        returned_ids = [
            note["id"]
            for note in response.data
        ]

        self.assertIn(
            self.note.id,
            returned_ids,
        )

        self.assertNotIn(
            self.other_note.id,
            returned_ids,
        )

    def test_authenticated_user_can_get_note_detail(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.get(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["id"],
            self.note.id,
        )

        self.assertEqual(
            response.data["title"],
            "My first note",
        )

    def test_user_cannot_get_another_users_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.get(
            self.other_note_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_authenticated_user_can_create_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        payload = {
            "title": "Created through API",
            "text": "This note was created by a test.",
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            Note.objects.filter(
                title="Created through API",
                user=self.user,
            ).exists()
        )

    def test_authenticated_user_can_patch_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        payload = {
            "title": "Updated title",
        }

        response = self.client.patch(
            self.detail_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.note.refresh_from_db()

        self.assertEqual(
            self.note.title,
            "Updated title",
        )

        self.assertEqual(
            self.note.text,
            "This is my first note.",
        )

    def test_user_cannot_patch_another_users_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        payload = {
            "title": "Trying to change someone else's note",
        }

        response = self.client.patch(
            self.other_note_url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

        self.other_note.refresh_from_db()

        self.assertEqual(
            self.other_note.title,
            "Private note",
        )

    def test_authenticated_user_can_delete_own_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.delete(
            self.detail_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertFalse(
            Note.objects.filter(
                id=self.note.id,
            ).exists()
        )

    def test_user_cannot_delete_another_users_note(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.delete(
            self.other_note_url,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

        self.assertTrue(
            Note.objects.filter(
                id=self.other_note.id,
            ).exists()
        )

    def test_anonymous_user_cannot_get_notes(self):
        response = self.client.get(
            self.list_url,
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

# Create your tests here.
