
# from flashcardApp.models import flashCard
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

#signupform
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# class CreateflashCard(forms.ModelForm):
#     # question = forms.CharField(label = "Question", max_length=200)
#     # answer = forms.CharField(label = "Answer",widget = forms.Textarea )
#      class Meta:
#         model = flashCard
#         fields = ['deck','question','answer']