# Generated by Django 2.2.3 on 2019-07-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('channel', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=50)),
                ('impressions', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('installs', models.PositiveIntegerField(default=0)),
                ('spend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
