from django.urls import path
from . import views
urlpatterns=[path('',views.homepage,name='homepage'),
             path('booktickets',views.booktickets,name='bookticket')]