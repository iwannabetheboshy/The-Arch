# Generated by Django 4.1 on 2022-08-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_alter_contact_city_alter_contact_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]