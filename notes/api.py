from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def notes_api(request):

    if request.method == "GET":
        notes = Note.objects.filter(user=request.user)

        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def note_detail_api(request, note_id):
    try:
        note = Note.objects.get(
            id=note_id,
            user=request.user
        )
    except Note.DoesNotExist:
        return Response(
            {"error": "Note not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = NoteSerializer(note)
    return Response(serializer.data)

