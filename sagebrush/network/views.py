# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from sagebrush.network.models import Person, FamilyMemberRelationship, Event, EventAttendance, Location
from sagebrush.network.serializers import PersonSerializer, FamilyMemberRelationshipSerializer, EventSerializer, EventAttendanceSerializer, LocationSerializer

class NetworkViewSet(viewsets.ViewSet):
    def list(self, request):
        people = Person.objects.all()
        relationships = FamilyMemberRelationship.objects.all()
        events = Event.objects.all()
        event_attendances = EventAttendance.objects.all()

        nodes = PersonSerializer(people, many=True).data
        links = FamilyMemberRelationshipSerializer(relationships, many=True).data
        event_nodes = EventSerializer(events, many=True).data
        event_links = EventAttendanceSerializer(event_attendances, many=True).data

        data = {
            'nodes': nodes,
            'links': links,
            'event_nodes': event_nodes,
            'event_links': event_links,
        }

        return Response(data)

class MapViewSet(viewsets.ViewSet):
    def list(self, request):
        locations = Location.objects.all()
        location_data = LocationSerializer(locations, many=True).data

        data = {
            'locations': location_data,
        }

        return Response(data)