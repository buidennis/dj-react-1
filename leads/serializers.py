from rest_framework import serializers
from .models import Lead

'''
    ModelSerializer
        & Subclassed
        & Suitable when close mapping between Model and Serializer is needed
'''
class LeadSerializer( serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')
