from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    




class Flashcard(models.Model):

    title = models.CharField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description =models.TextField()
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    date= models.DateField()

    def __str__(self):
        return self.title


    def save_flashcard(self):
        self.save()

    def delete_flashcard(self):
        self.delete()          

# class deck(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deck", null=True)
#     name = models.CharField(max_length=200)
    

#     def __str__(self):
#         return self.name

# class flashCard(models.Model):
#     deck = models.ForeignKey(deck, on_delete=models.CASCADE, related_name="flashCard", null=True)
#     question = models.CharField(max_length = 200)
#     answer = models.TextField()
    

#     def __str__(self):
#         return self.question