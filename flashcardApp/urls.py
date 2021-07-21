
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import FlashcardView

urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('api/flashcard/', FlashcardView.as_view(), name='FlashcardView'),
    # url(r'^api/v1/posts/$', 'post_collection'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)