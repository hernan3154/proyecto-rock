# Generated by Django 4.2.9 on 2024-04-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0024_rename_photo_indio_solari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indio_solari',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]