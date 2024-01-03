# Generated by Django 4.2.4 on 2023-08-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_post', models.CharField(max_length=255)),
                ('body_post', models.TextField()),
                ('category', models.CharField(choices=[('TNK', 'Танки'), ('HIL', 'Хилы'), ('DD', 'ДД'), ('MCH', 'Торговцы'), ('GMA', 'Гилдмастеры'), ('QMA', 'Квестгиверы'), ('BLM', 'Кузнецы'), ('TAN', 'Кожевники'), ('PMK', 'Зельевары'), ('SMA', 'Мастера заклинаний')], default='TNK', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
