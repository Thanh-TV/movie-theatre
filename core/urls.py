from django.conf.urls import url, include
from rest_framework import routers
from .views.movie import MovieViewSet
from .views.room import RoomViewSet
from .views.room_booking import RoomBookingViewSet
from .views.ticket import TicketViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'movie', MovieViewSet, base_name="movie")
router.register(r'room', RoomViewSet, base_name="room")
router.register(r'room_booking', RoomBookingViewSet, base_name="room_booking")
router.register(r'ticket', TicketViewSet, base_name="ticket")

urlpatterns = [
    url(r'^', include(router.urls)),
]
