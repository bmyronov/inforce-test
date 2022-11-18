import datetime

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from vote.models import Vote
from vote.permissions import UserHasntVoted
from vote.serializers import VoteSerializer


class VoteCreateView(generics.ListCreateAPIView):
    today = datetime.date.today()
    queryset = Vote.objects.filter(date=today)
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated, UserHasntVoted)
