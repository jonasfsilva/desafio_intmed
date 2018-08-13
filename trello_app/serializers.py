from rest_framework import serializers
from trello_app.models import WebHookReceived


class WebHookSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebHookReceived
        fields = '__all__'