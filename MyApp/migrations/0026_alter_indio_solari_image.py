# Generated by Django 4.2.9 on 2024-04-11 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0025_alter_indio_solari_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indio_solari',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Indio_ solaris/'),
        ),
    ]
