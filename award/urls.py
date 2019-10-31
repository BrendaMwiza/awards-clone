from django.conf.urls import url,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name ='welcome'),
    url(r'^new/picture$', views.new_pic, name='addPic'),
    url(r'^profile/', views.getProfile, name='profile'),
    url(r'^editprofile',views.editProfile, name='editProfile'),
    url(r'^rating/',views.rating,name="rates"),
    # url(r'^myprofile/$',views.profiled,name="profiled"),
    # url(r'^point/$',views.point,name="point"),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/image/$',views.ImageList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)