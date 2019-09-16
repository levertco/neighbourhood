from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
url(r'^$',views.index,name='index'), 

url(r'^upload/',views.upload, name='upload'),
url(r'^posts/',views.post,name='post'),
url(r'^group/',views.group,name='group'),
url(r'^search/', views.search_results, name='search_results'),
url(r'^single_profile/',views.single_profile, name='single_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)