from rest_framework import serializers
from app1.models import  Message2WhatApp

class Message2WhatAppSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Message2WhatApp
        fields = ('to_number','message')
