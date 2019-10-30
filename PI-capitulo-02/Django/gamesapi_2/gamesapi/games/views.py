from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GamesView(APIView):

    def get(self, request):
        Response(status=status.HTTP_200_OK)

    def post(self, request):
        Response(status=status.HTTP_200_OK)
