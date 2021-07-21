from django.contrib import admin

# Register your models here.
from . models import Subject, Flashcard
admin.site.register(Subject)
admin.site.register(Flashcard)
