from django.contrib import admin

from .models import (
    Alias,
    Event,
    EventAttendance,
    FamilyMemberRelationship,
    Location,
    Organization,
    Person,
    PoliticalAffiliation,
)


class RelationshipInline(admin.TabularInline):
    model = FamilyMemberRelationship
    fk_name = "person"
    extra = 1


class EventsInline(admin.TabularInline):
    model = EventAttendance
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline, EventsInline]
    list_display = ("get_full_name", "occupation", "dob", "dod", "home")
    list_filter = ["last_name", "dob", "dod", "home", "farm_ranch_location"]


@admin.register(Alias)
class AliasAdmin(admin.ModelAdmin):
    pass


@admin.register(PoliticalAffiliation)
class PoliticalAffiliationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(FamilyMemberRelationship)
