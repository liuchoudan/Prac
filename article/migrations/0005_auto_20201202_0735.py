# Generated by Django 3.1.3 on 2020-12-02 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_hobby_student'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='hobby',
            table='hobby',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
