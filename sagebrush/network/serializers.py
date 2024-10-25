# serializers.py
from rest_framework import serializers
from sagebrush.network.models import Person, FamilyMemberRelationship, Event, EventAttendance, Location

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name']

class FamilyMemberRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMemberRelationship
        fields = ['person', 'related', 'relation_type']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date_start', 'date_end']

class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ['event', 'person']

class LocationSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    people = PersonSerializer(many=True, read_only=True, source='residents')

    class Meta:
        model = Location
        fields = ['id', 'city', 'state', 'address', 'latitude', 'longitude', 'events', 'people']