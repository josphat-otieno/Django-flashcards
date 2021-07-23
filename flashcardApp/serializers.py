from rest_framework import serializers
from  .models import Subject, Flashcard


# class SubjectListPageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)

class FlashcardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    flash_title = serializers.CharField()
    flash_notes = serializers.CharField()

    def create(self, validated_data):
        return Flashcard.objects.create(**validated_data)

class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject_name=serializers.CharField()

    flashcards = FlashcardSerializer(many=True, read_only=True)
    flashcard = FlashcardSerializer(write_only=True, required=False)

    # verbose_subject_name = serializers.CharField(read_only=True)
    # DRF serializer.save() calls self.create(self.validated_data)
    def create(self, validated_data):
        flash_dict =validated_data['flashcard']
        subject = Subject.objects.create(**validated_data)
        flash_dict['subject']=subject
        Flashcard.objects.create(**flash_dict)
        return subject

    def update(self, instance, validated_data):
        for key,value in validated_data.items():
            setattr(instance,key, value)
        instance.save()
        return instance

