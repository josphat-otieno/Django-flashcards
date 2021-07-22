from django.contrib.auth.views import UserModel
from django.http.response import Http404
from flashcardApp.serializers import CardSerializer, CategorySerializer, UserSerializer
from flashcardApp.models import Category, Flashcard
from flashcardApp.forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render( request,'index.html')
def profile(request):
    return render( request,'index.html')



def register(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})
    

# def createFlash(response, id):
#     form = CreateflashCard()
#     s_deck = get_object_or_404(deck, id=id)
#     if not response.user.is_authenticated:
#         return HttpResponseRedirect("/")
#     if s_deck not in response.user.deck.all():
#         return HttpResponseRedirect("/")
#     if response.method == "POST":
#         form = CreateflashCard(response.POST)
#         if form.is_valid():
#             card = flashCard(deck = s_deck,question = form.cleaned_data["question"],answer = form.cleaned_data["answer"])
#             card.save() 
#         form = CreateflashCard()
#     context = {"id":id,"deck":s_deck, "form":form}
#     return render(response, "flashcreate.html", context)





class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        profiles = Category.objects.all()
        serializer = CategorySerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CategoryDetail(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlashcardList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        projects =Flashcard.objects.all()
        serializer = CardSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        profiles =User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        