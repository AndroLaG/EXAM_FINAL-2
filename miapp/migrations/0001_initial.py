# Generated by Django 5.0.6 on 2024-07-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sanchez_Tucta_Persona",
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
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("sexo", models.CharField(max_length=1)),
                ("fecha_de_registro", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
