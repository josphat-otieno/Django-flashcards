from django.db import models

# Create your models here

class Subject(models.Model):
    subject_name = models.CharField(max_length=60)

    def __str__(self):
        return self.subject_name

    def save_subject(self):
        self.save()

    def delete_subject(self):
        self.delete()

class Flashcard(models.Model):
    flash_image = models.ImageField(upload_to='images/')
    flash_title = models.CharField(max_length=60 )
    flash_notes = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.flash_title