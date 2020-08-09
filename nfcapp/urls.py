from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('videos',views.videos,name='videos'),
    path('stories',views.stories,name = 'stories'),
    path('add-story',views.add_story,name = 'add_story'),
    path('login', views.login, name= "login"),
    path('auth', views.authenticate, name="auth"),
    path('signup', views.signup, name = 'signup'),
    path('register', views.register, name='regsiter'),
    path('logout', views.logout, name="logout"),
    path('page/<n>', views.next_page, name = 'next_page')
]
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)