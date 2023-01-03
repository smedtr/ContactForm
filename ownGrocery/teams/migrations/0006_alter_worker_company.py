# Generated by Django 4.1.4 on 2023-01-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_worker_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='company',
            field=models.CharField(choices=[('KYND-BE', 'Kyndryl BE'), ('PISQ-BE', 'PI-SQUARE')], db_index=True, max_length=7),
        ),
    ]