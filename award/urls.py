from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name ='welcome'),
    url(r'^new/picture$', views.new_pic, name='addPic'),
    url(r'^profile/', views.getProfile, name='profile'),
    url(r'^editprofile',views.editProfile, name='editProfile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)