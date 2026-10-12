from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def notes_api(request):
    notes = Note.objects.filter(user=request.user)

    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)
