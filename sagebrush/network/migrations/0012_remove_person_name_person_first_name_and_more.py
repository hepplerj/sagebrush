# Generated by Django 4.2.11 on 2024-04-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0011_alter_familymemberrelationship_relation_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="name",
        ),
        migrations.AddField(
            model_name="person",
            name="first_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="last_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="middle_name_or_initial",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="familymemberrelationship",
            name="relation_type",
            field=models.CharField(
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
                    ("Grandparent", "Grandparent"),
                    ("Grandchild", "Grandchild"),
                    ("Aunt/Uncle", "Aunt/Uncle"),
                    ("Niece/Nephew", "Niece/Nephew"),
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
    ]
