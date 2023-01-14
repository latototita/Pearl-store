# Generated by Django 3.2 on 2023-01-14 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_file_download_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/movies')),
                ('description', models.TextField(max_length=1000)),
                ('download_link', models.CharField(blank=True, max_length=100, null=True)),
                ('seriename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seriesname')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.type')),
            ],
        ),
    ]
