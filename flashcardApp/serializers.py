from django.db.models import fields
from django.db.models.fields import CharField
from rest_framework import generics, serializers
from .models import Subject,Flashcard
from flashcardApp import models



class FlashcardSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.filter(), slug_field='subject_name'
    )
    class Meta:
        model = Flashcard
        fields = ('id', 'subject' ,'flash_title', 'flash_notes', )


        # flash_title = serializers.CharField()
        # flash_notes= serializers.CharField()
        # subject_id = serializers.IntegerField()
        
        
        def create(self, validated_data):
            return Flashcard.objects.create(**validated_data)


class SubjectSerializer(serializers.Serializer):
        subject_name=serializers.CharField()

        verbose_subject_name = serializers.CharField(read_only=True)
        # DRF serializer.save() calls self.create(self.validated_data)
        def create(self, validated_data):
            return Subject.objects.create(**validated_data)

        def update(self, instance, validated_data):
            for key,value in validated_data.items():
                setattr(instance,key, value)
                instance.save()
            return instance
        
    # def update(self, instance, validated_data):
    #     instance.flash_title = validated_data.get('flash_title', instance.flash_title)
    #     instance.flash_notes = validated_data.get('flash_notes', instance.flash_notes)
    #     instance.subject_id = validated_data.get('subject_id', instance.subject_id)

    #     instance.save()
    #     return instance