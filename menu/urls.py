from django.urls import path

from menu.views import MenuCreateView, MenuDeleteView


urlpatterns = [
    path('', MenuCreateView.as_view()),
    path('<int:pk>', MenuDeleteView.as_view()),
]
