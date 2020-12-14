from app.viewsets import ticket_tableViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ticket_table',ticket_tableViewset)