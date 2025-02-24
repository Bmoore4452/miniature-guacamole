# Generated by Django 5.1.5 on 2025-02-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('options', models.JSONField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('level', models.IntegerField(choices=[(1, 'Current'), (2, 'Recent'), (3, 'Legend')])),
            ],
        ),
    ]
