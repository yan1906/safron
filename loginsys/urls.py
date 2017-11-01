from django.conf.urls import url
from django.contrib import admin
# from article import views as article_views
from loginsys import views as loginsys_views

urlpatterns = [
 	url(r'^login/', loginsys_views.login), 
 	url(r'^logout/', loginsys_views.logout), 
 	url(r'^register/', loginsys_views.register), 

]


	