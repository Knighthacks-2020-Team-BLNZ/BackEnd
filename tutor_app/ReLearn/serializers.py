from rest_framework import serializers
from .models import ReLearn

class ReLearnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReLearn
        fields = ('user_name', 'user_type', 'user_personality', 'user_writeup')