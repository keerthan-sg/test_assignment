
# import model from models.py
from .models import ticket_table
from rest_framework import serializers
# Create a model serializer
class ticket_tableSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = ticket_table
		fields = '__all__'
