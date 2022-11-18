import datetime

from rest_framework import permissions

from authentication.models import Employee


class UserHasntVoted(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        employee = Employee.objects.get(user_id=request.user.id)

        return bool(employee.last_vote_time != datetime.date.today())
