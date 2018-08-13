from django.shortcuts import render
from rest_framework.views import APIView
from loja.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from trello_app.models import WebHookReceived
from trello_app.serializers import WebHookSerializer
from rest_framework import viewsets
from rest_framework import serializers


class WebHookTrelloView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request, format=None):
        """
        Return 
        """
        queryset = WebHookReceived.objects.all()
        serializer_class = WebHookSerializer
        serializer = serializer_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):        
        """
        POST received
        """
        jsondata = request.body
        data = json.loads(jsondata)
        
        WebHookReceived.objects.create(
            data=data
        )

        return Response([])


# class WebHookReceivedViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     List all WebHookReceived
#     """
#     queryset = WebHookReceived.objects.all()
#     serializer_class = WebHookSerializer
#     permission_classes = (IsAdmin,)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)