from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from contacts.models import NewContact
from rest_api.serializers import ( NewContactSerializers)


class NewContacts(APIView):

    def get(self, request):
        rooms = NewContact.objects.all()
        serializer = NewContactserializers(rooms, many=True)
        return Response({"data": serializer.data})

