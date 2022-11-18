from django.urls import path

from vote.views import VoteCreateView


urlpatterns = [
    path('', VoteCreateView.as_view()),
]
