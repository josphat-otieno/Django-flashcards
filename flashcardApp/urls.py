from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index, name='index'),
    # url('register/',views.register, name='registration'),
    url('register/', views.register, name='signup'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'),
    # url("createflash-<int:id>", views.createFlash, name = "createFlash" ),

       #api endpoints
    url('api/category',views.CategoryList.as_view(),name='categoryEndpoint'),
    url('api/flashcards',views.FlashcardList.as_view(),name='flashcardEndpoint'),
    url('api/user',views.UserList.as_view(),name='userEndpoint'),
    url('api/category/<int:pk>/',views.CategoryDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)