# Generated by Django 5.0 on 2023-12-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0006_remove_place_id_alter_place_night_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.IntegerField()),
                ('Message', models.TextField()),
            ],
        ),
    ]
