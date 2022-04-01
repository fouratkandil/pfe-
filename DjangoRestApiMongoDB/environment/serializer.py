from rest_framework import serializers
from environment.models import Environment

class enironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('id',
                  'title',
                  'type',
                  'location')