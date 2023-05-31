# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    # This is a list of dictionaries for api endpoints
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
        {
            'Endpoint': '/notes/id/get',
            'method': 'GET',
            'body': None,
            'description': 'Gets query param from url'
        }
    ]
    #  safe=False is to allow non-dict objects to be serialized (turned) into JSON
    # return JsonResponse(routes, safe=False)

    #! Response is a wrapper for JsonResponse
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    #! Serialize the note
    # many=True is for a list of objects
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    #! Serialize the note
    # Many=False is for a single object
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    #! request.data is the data sent in the post request
    data = request.data
    #! Create a new note
    note = Note.objects.create(
        body=data['body']
    )
    #! Serialize the note
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    #! request.data is the data sent in the post request
    data = request.data
    #! Get the note
    note = Note.objects.get(id=pk)
    #! Serialize the note
    # data is the data sent in the request
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    #! Get the note
    note = Note.objects.get(id=pk)
    #! Delete the note
    note.delete()
    return Response("Note was deleted")
