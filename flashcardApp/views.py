
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import  Subject, Flashcard
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import FlashcardSerializer, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics


# Create your views here.

def index(request):
    flashcards = Flashcard.objects.all()

    return render (request, 'index.html', {"flashcards": flashcards})



@api_view(['GET','POST',])
def flash_view(request):
    if request.method =='GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectSerializer(data = request.data)
        if serializer.is_valid():
            # subject_name = serializer.data['subject_name']
            # Subject.objects.create(**serializer.validated_data)
            subject = serializer.save()
            return Response(SubjectSerializer(subject).data, status=status.HTTP_201_CREATED)
            # return Response("Subject added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH', 'DELETE'])
def flash_detail_view(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            subject = serializer.save()
            return Response(SubjectSerializer(subject).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # raise NotImplementedError("Patch currently not supported")

    elif request.method == 'DELETE':
        subject.delete()
        return Response ("Subject deleted", status=status.HTTP_204_NO_CONTENT)
        # raise NotImplementedError("DELETE currenty not supported")

@api_view(['POST'])      
def flashcard_view(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    serializer = FlashcardSerializer(data=request.data)
    if serializer.is_valid():
        flashcard = serializer.save(subject=subject)
        return Response(FlashcardSerializer(flashcard).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FlashcardView(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class =FlashcardSerializer

class FlashMember(generics.RetrieveDestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


# class FlashcardView(ListModelMixin, CreateModelMixin, GenericAPIView, ):
#     queryset = Flashcard.objects.all()
# #     serializer_class=FlashcardSerializer

#     def perform_create(self, serializer):
#         subject_name = get_object_or_404(Subject, id=self.request.data.get('subject_id'))
#         return serializer.save(subject_name=subject_name)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(self, request, *args, **kwargs)

# class SingleFlashcardView(RetrieveAPIView):
#         queryset = Flashcard.objects.all()
#         serializer_class = FlashcardSerializer

    # def put(self, request, *args, **kwargs):
    #     return self.update(self, request, *args, **kwargs)

    

    # def patch(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
# class FlashcardView(APIView):
    
#     def get(self, request):
#         flashcards = Flashcard.objects.all()
#         serializer= serializers.FlashcardSerializer(flashcards, many= True)
#         return Response({"flashcards": serializer.data})

#     def post(self, request):
#         flashcard = request.data.get('flashcard')

#         serializer = FlashcardSerializer(data=flashcard)
#         if serializer.is_valid(raise_exception=True):
#             flashcard_saved = serializer.save()
#         return Response({"success": "Flashcard '{}' created successfully".format(flashcard_saved.flash_title)})

#     def put(self, request,pk):
#         saved_flashcard = get_object_or_404(Flashcard.objects.all(),pk=pk)
#         data = request.data('flashcard')
#         serializer=FlashcardSerializer(instance=saved_flashcard, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             flashcard_saved = serializer.save()
#         return Response({"success": "Flashcard '{} updated successfully".format(flashcard_saved.flash_title)})

#     def delete(self, request, pk):
#         flashcard = get_object_or_404(Flashcard.objects.all(), pk=pk)
#         flashcard.delete()
#         return Response({"message": "Flashcard with id `{}` has been deleted.".format(pk)},status=204)

