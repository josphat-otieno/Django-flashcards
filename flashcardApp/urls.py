
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import FlashcardView

urlpatterns = [
    path('flashcard/', FlashcardView.as_view()),
    # url(r'^api/v1/posts/$', 'post_collection'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)