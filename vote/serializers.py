import datetime

from authentication.models import Employee

from rest_framework import serializers

from vote.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('menu', 'likes')

    def create(self, validated_data):
        # Getting restaurant_id
        user = self.context['request'].user

        # Getting menu id
        menu = validated_data.pop('menu')
        vote, _ = Vote.objects.get_or_create(menu=menu)
        vote.likes += 1
        vote.save()

        # Making sure employee can't vote again today
        today = datetime.date.today()
        employee = Employee.objects.get(user_id=user)
        employee.last_vote_time = today
        employee.save()

        return vote
