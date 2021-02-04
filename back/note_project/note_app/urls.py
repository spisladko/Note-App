from django.urls import path, include
from .views import *

app_name = "note_app"

urlpatterns = [
    path('notes/', NotesAPIView.as_view()),
    path('notes/<int:pk>', NoteAPIView.as_view()),
    path('notes/<int:pk>/delete', NoteAPIDelete.as_view()),
    path('notes/<int:pk>/update', NoteAPIUpdate.as_view()),
    path('notes/create', NoteCreateView.as_view()),
]

