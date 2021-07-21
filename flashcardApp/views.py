from flashcardApp import serializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import  Subject, Flashcard
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import FlashcardSerializer
from datetime import datetime
from rest_framework.views import APIView

from django.http import HttpResponse
# Create your views here.

def index(request):
    flashcards = Flashcard.objects.all()

    return render (request, 'index.html', {"flashcards": flashcards})

class FlashcardView(APIView):
    def get(self, request):
        flashcards = Flashcard.objects.all()
        serializer= serializers.FlashcardSerializer(flashcards, many= True)
        return Response({"flashcards": serializer.data})

    def post(self, request):
        flashcard = request.data.get('flashcard')

        serializer = FlashcardSerializer(data=flashcard)
        if serializer.is_valid(raise_exception=True):
            flashcard_saved = serializer.save()
        return Response({"success": "Flashcard '{}' created successfully".format(flashcard_saved.flash_title)})
