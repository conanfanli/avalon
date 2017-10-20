from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from .views import MissionViewSet, VoteViewSet


router = routers.DefaultRouter()

router.register(r'missions', MissionViewSet, base_name='mission')
router.register(r'votes', VoteViewSet)

urlpatterns = router.urls + [
    url(r'^tokens/', obtain_jwt_token),
]
