from django.urls import path
from . import views
# -*- coding: utf-8 -*-

urlpatterns = [
    path('update_comment',views.update_comment,name="update_comment"),
]
