import datetime

from menu.models import Menu
from menu.permissions import CreateMemuPermission, IsOwnerOrReadOnly
from menu.serializers import MenuSerializer

from rest_framework import generics


class MenuCreateView(generics.ListCreateAPIView):
    today = datetime.date.today()
    queryset = Menu.objects.filter(date_serverd=today)
    serializer_class = MenuSerializer
    permission_classes = (CreateMemuPermission,)

    # All employees can see menus
    # Restaurants can only see their own menus
    def get_queryset(self):
        if self.request.method == 'GET':
            user = self.request.user

            if user.is_employee:
                today = datetime.date.today()
                return Menu.objects.filter(date_serverd=today)
            else:
                return Menu.objects.filter(restaurant=user)


class MenuDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrReadOnly,)
