# Generated by Django 3.2.18 on 2023-03-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0002_alter_townhallselection_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='townhallselection',
            name='thumbnail',
            field=models.ImageField(upload_to='townhall/'),
        ),
    ]
