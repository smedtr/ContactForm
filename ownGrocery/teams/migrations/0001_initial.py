# Generated by Django 4.1.4 on 2023-01-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrgUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('HI', 'Hierarchical Unit'), ('FU', 'Functional Unit')], db_index=True, max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('starting_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('ending_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='teams.orgunit', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'org_unit',
                'verbose_name_plural': 'org_units',
            },
        ),
    ]
