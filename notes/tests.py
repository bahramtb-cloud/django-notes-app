from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

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

# Create your tests here.
