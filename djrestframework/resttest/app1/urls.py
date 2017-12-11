from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views

urlpatterns = [
    # path('snippets/',views.snippet_list),
    # path('snippets/<int:pk>/',views.snippet_detail),

    #2.0 使用基于泛类(generic class)的视图
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>/',views.SnippetDetail.as_view()),

    path('users/',views.UserList.as_view()),
    path('users/<int:pk>/',views.UserDetail.as_view()),    
]

urlpatterns=format_suffix_patterns(urlpatterns)