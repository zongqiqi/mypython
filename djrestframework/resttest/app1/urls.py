from django.urls import path
from app1 import views

urlpatterns = [
    path('^snippets/$',views.snippet_list),
    path('^snippets/<int:pk>/$',views.snippet_detail),
]