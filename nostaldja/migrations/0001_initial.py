# Generated by Django 4.2.7 on 2023-11-16 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decades', to='nostaldja.decade')),
            ],
        ),
    ]
