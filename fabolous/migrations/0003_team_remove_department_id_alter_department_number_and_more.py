# Generated by Django 5.2 on 2025-04-30 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabolous', '0002_department_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=30)),
                ('team_Summary', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Health_Check_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('green', 'Green'), ('amber', 'Amber'), ('red', 'Red')], max_length=10, null=True)),
                ('comments', models.TextField(blank=True)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabolous.team')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=40)),
                ('fullName', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('team_leaderFlag', models.BooleanField(default=False)),
                ('team_leaderId', models.CharField(blank=True, max_length=20, null=True)),
                ('roles_flag', models.BooleanField(default=True)),
                ('roles', models.CharField(max_length=100, null=True)),
                ('engineer_flag', models.BooleanField(default=True)),
                ('engineer_id', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabolous.department')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabolous.user'),
        ),
    ]
