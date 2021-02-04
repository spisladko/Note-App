from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "name", "description", "creation_date"]
        read_only_fields = ["creation_date"]
        

class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "name", "description", "creation_date"]