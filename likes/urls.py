from django.urls import path
from . import views
# -*- coding: utf-8 -*-

urlpatterns = [
    path('like_change',views.like_change,name="like_change"),
]
