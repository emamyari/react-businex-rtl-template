# Generated by Django 4.1.7 on 2023-05-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_maping"),
    ]

    operations = [
        migrations.RemoveField(model_name="maping", name="color",),
        migrations.AlterModelTable(name="maping", table="tbl_maping",),
    ]
