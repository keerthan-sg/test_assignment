from  rest_framework import viewsets
from . import models
from . import serializers

class  ticket_tableViewset(viewsets.ModelViewSet):
    queryset = models.ticket_table.objects.all()
    serializer_class = serializers.ticket_tableSerializer


