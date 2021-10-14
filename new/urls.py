from django.urls import path
from . views import ProgrammingNewsApiView

urlpatterns = [
     path('', ProgrammingNewsApiView.as_view()),
     path('api/<int:id>/', ProgrammingNewsApiView.as_view())
]