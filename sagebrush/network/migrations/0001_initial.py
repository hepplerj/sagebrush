# Generated by Django 5.0.4 on 2024-05-07 13:44

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Alias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "verbose_name_plural": "Aliases",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("date_start", models.DateField(blank=True, null=True)),
                ("date_end", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="FamilyMemberRelationship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relation_type",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Occupation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PoliticalAffiliation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
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
                        ],
                        default=1,
                        max_length=2,
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=100)),
                (
                    "events",
                    models.ManyToManyField(
                        blank=True,
                        related_name="locations",
                        to="network.event",
                        verbose_name="Known events at this location",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="event_location",
                to="network.location",
            ),
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=255)),
                (
                    "middle_name_or_initial",
                    models.CharField(blank=True, max_length=255),
                ),
                ("last_name", models.CharField(blank=True, max_length=255)),
                (
                    "dob",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Birth"
                    ),
                ),
                (
                    "dod",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Death"
                    ),
                ),
                (
                    "photograph",
                    models.ImageField(
                        blank=True, default="unknown.jpg", null=True, upload_to=""
                    ),
                ),
                ("occupation", models.CharField(blank=True, max_length=255, null=True)),
                ("criminal_charges", models.BooleanField(blank=True, default=False)),
                ("criminal_charges_notes", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("aliases", models.ManyToManyField(blank=True, to="network.alias")),
                (
                    "collaborators",
                    models.ManyToManyField(
                        blank=True,
                        to="network.person",
                        verbose_name="Known collaborators",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "farm_ranch_location",
                    models.ManyToManyField(
                        blank=True,
                        related_name="farmers_ranchers",
                        to="network.location",
                        verbose_name="Farm or ranch location(s)",
                    ),
                ),
                (
                    "home",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="residents",
                        to="network.location",
                    ),
                ),
                (
                    "relatives",
                    models.ManyToManyField(
                        blank=True,
                        through="network.FamilyMemberRelationship",
                        to="network.person",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "political_affiliations",
                    models.ManyToManyField(
                        blank=True, to="network.politicalaffiliation"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="organizations", to="network.person"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OccupationHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "occupation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="network.occupation",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="network.person"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FederalOrganization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True,
                        related_name="federal_organizations",
                        to="network.person",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="familymemberrelationship",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="relationships",
                to="network.person",
            ),
        ),
        migrations.AddField(
            model_name="familymemberrelationship",
            name="related",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reverse_relationships",
                to="network.person",
            ),
        ),
        migrations.CreateModel(
            name="EventAttendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendees",
                        to="network.event",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attended_events",
                        to="network.person",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                related_name="events",
                through="network.EventAttendance",
                to="network.person",
            ),
        ),
    ]
