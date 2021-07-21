from rest_framework import serializers
from .models import Subject,Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='subject_name'
    )

    class Meta:
        model = Flashcard
        fields = ('id', 'subject', 'flash_title', 'flash_notes', 'created', 'updated')
