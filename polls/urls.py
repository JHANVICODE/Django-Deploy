from django.urls import path
from .views import ping

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_detail")
    path("ping/",ping,name="ping")
]