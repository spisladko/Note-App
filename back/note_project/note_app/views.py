from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import requests
from datetime import datetime, timedelta
import pytz

class NotesAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        username = self.request.user
        
        return Note.objects.filter(owner=username)
        
class NoteAPIView(generics.RetrieveAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    

class NoteAPIDelete(generics.RetrieveDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    
class NoteAPIUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    
class NoteCreateView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        description = request.data.get("description")
        owner = self.request.user
        creation_date = datetime.now() + timedelta(hours=3)
        note = Note.objects.create(name=name, description=description, owner=owner, creation_date=creation_date)
        return Response("Заметка создана", status=200)