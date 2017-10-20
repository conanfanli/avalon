from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from .views import VoteViewSet, MissionViewSet


router = routers.DefaultRouter()

router.register(r'votes', VoteViewSet)
router.register(r'missions', MissionViewSet)

urlpatterns = router.urls + [
    url(r'^tokens/', obtain_jwt_token),
]
