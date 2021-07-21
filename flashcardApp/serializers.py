from django.db.models.fields import CharField
from rest_framework import serializers
from .models import Subject,Flashcard
from flashcardApp import models


class FlashcardSerializer(serializers.Serializer):
    flash_title = serializers.CharField()
    flash_notes= serializers.CharField()
    subject_id = serializers.IntegerField()

    def create(self, validated_data):
        return Flashcard.objects.create(**validated_data)
    