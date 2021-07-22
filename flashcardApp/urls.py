
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import FlashcardView, FlashMember

urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('api/flashcard/', FlashcardView.as_view(), name='FlashcardView'),
    path('api/flashcards/(?P<pk>[0-9]+)/$',FlashMember.as_view()),
    path('api/subjects/<int:subject_id>/', views.flash_detail_view, name='flash_detail_view'),
    path('api/subjects/<int:subject_id>/flashcards/', views.flashcard_view, name='flashcard_view')
    # path('api/flashcard/<int:pk>', FlashcardView.as_view()),
    # path('api/flashcard/<int:pk>', SingleFlashcardView.as_view()),
    # url(r'^api/v1/posts/$', 'post_collection'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)