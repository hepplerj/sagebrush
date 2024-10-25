from datetime import date

from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager

import logging

logger = logging.getLogger(__name__)

class Person(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    middle_name_or_initial = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    aliases = models.ManyToManyField("Alias", blank=True)
    dob = models.DateField(
        verbose_name="Date of Birth",
        blank=True,
        null=True,
    )
    dod = models.DateField(
        verbose_name="Date of Death",
        blank=True,
        null=True,
    )
    photograph = models.ImageField(
        default="unknown.jpg",
        blank=True,
        null=True,
    )
    political_affiliations = models.ManyToManyField(
        "PoliticalAffiliation",
        blank=True,
    )
    criminal_charges = models.BooleanField(
        default=False,
        blank=True,
    )
    criminal_charges_notes = models.TextField(blank=True)
    collaborators = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name="Known collaborators",
    )
    home = models.ForeignKey(
        "Location",
        on_delete=models.PROTECT,
        related_name="residents",
        default=1,
        blank=True,
        null=True,
    )
    farm_ranch_location = models.ManyToManyField(
        "Location",
        related_name="farmers_ranchers",
        blank=True,
        verbose_name="Farm or ranch location(s)",
    )
    notes = models.TextField(blank=True)
    relatives = models.ManyToManyField(
        "self",
        through="network.FamilyMemberRelationship",
        through_fields=("person", "related"),
        blank=True,
        symmetrical=False,
    )
    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def calculate_age(self):
        delta = self.dod - self.dob if self.dod else date.today() - self.dob
        return delta.days // 365


class Alias(models.Model):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Aliases"

    def __str__(self):
        return self.name


class PoliticalAffiliation(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class FamilyMemberRelationship(models.Model):
    RELATIONSHIP_TYPES = [
        ("Parent", "Parent"),
        ("Child", "Child"),
        ("Sibling", "Sibling"),
        ("Spouse", "Spouse"),
        ("Partner", "Partner"),
        ("Friend", "Friend"),
        ("Colleague", "Colleague"),
        ("Mentor", "Mentor"),
        ("Student", "Student"),
        ("Teacher", "Teacher"),
        ("Business Partner", "Business Partner"),
        ("Grandparent", "Grandparent"),
        ("Grandchild", "Grandchild"),
        ("Aunt", "Aunt"),
        ("Uncle", "Uncle"),
        ("Niece", "Niece"),
        ("Nephew", "Nephew"),
        ("Cousin", "Cousin"),
        ("Guardian", "Guardian"),
        ("Caretaker", "Caretaker"),
        ("Roommate", "Roommate"),
        ("Neighbor", "Neighbor"),
        ("Acquaintance", "Acquaintance"),
    ]

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="relationships",
    )
    related = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="reverse_relationships",
    )
    relation_type = models.CharField(
        max_length=255,
        blank=True,
        choices=RELATIONSHIP_TYPES,
    )

    def __str__(self) -> str:
        return f"{self.related} is a {self.relation_type} of {self.person}"


class Location(models.Model):
    STATES = (
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
        ("Un", "Unknown"),
    )

    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, choices=STATES, default=1)
    address = models.CharField(max_length=100, blank=True)
    events = models.ManyToManyField(
        "Event",
        related_name="locations",
        blank=True,
        verbose_name="Known events at this location",
    )
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.state == "Un":
            return "Unknown"
        return f"{self.city}, {self.state}"

    # On save, the following tries to derive the latlon from the town_city and country
    # fields. If successful, it stores the latlon in the latlon field.
    def save(self, *args, **kwargs):
        if self.latitude is None or self.longitude is None:
            try:
                from geopy.geocoders import Nominatim

                geolocator = Nominatim(user_agent="sagebrush")
                location_components = [
                    self.address,
                    self.city,
                    self.state,
                    "United States",
                ]
                location_string = " ".join(filter(None, location_components))
                location = geolocator.geocode(location_string)

                if location is not None:
                    self.latitude = str(location.latitude)
                    self.longitude = str(location.longitude)
            except Exception as e:
                logger.warning("Warning geocoding: " + str(e) + str(self))
        super().save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="event_location",
        default=1,
        blank=True,
    )
    participants = models.ManyToManyField(
        Person,
        related_name="events",
        blank=True,
        through="network.EventAttendance",
    )

    def __str__(self):
        return self.name


class EventAttendance(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="attendees",
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="attended_events",
    )

    def __str__(self):
        return f"{self.person} attended {self.event}"


class Organization(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, related_name="organizations")

    def __str__(self):
        return self.name


class FederalOrganization(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        Person,
        related_name="federal_organizations",
        blank=True,
    )

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OccupationHistory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Occupation Histories"

    def __str__(self):
        return (
            f"{self.person} - {self.occupation} ({self.start_date} - {self.end_date})"
        )
