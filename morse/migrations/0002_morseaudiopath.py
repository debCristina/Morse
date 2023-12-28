# Generated by Django 5.0 on 2023-12-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MorseAudioPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subname', models.CharField(max_length=50)),
                ('text_code', models.CharField(max_length=50)),
                ('audio_path', models.FileField(blank=True, null=True, upload_to='audio_morse_code')),
            ],
        ),
    ]
