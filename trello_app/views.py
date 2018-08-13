from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view



class WebHookTrelloView(APIView):
    
    def get(self, request, format=None):
        """
        Return 
        """
        return Response([])

    def post(self, request, format=None):        
        """
        POST received
        """
        return Response([])
