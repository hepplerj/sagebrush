from django.contrib import admin

from .models import (
    Alias,
    Occupation,
    OccupationHistory,
    Event,
    EventAttendance,
    FamilyMemberRelationship,
    FederalOrganization,
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


class EmploymentHistoryInline(admin.TabularInline):
    model = OccupationHistory
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline, EventsInline, EmploymentHistoryInline]
    list_display = ("get_full_name", "dob", "dod", "home")
    list_filter = ["last_name", "dob", "dod", "home", "farm_ranch_location", "events"]


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date_start", "date_end", "location")
    list_filter = ["date_start", "date_end", "location"]


@admin.register(Alias)
class AliasAdmin(admin.ModelAdmin):
    pass


@admin.register(PoliticalAffiliation)
class PoliticalAffiliationAdmin(admin.ModelAdmin):
    pass


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Organization)
admin.site.register(FederalOrganization)
admin.site.register(FamilyMemberRelationship)
