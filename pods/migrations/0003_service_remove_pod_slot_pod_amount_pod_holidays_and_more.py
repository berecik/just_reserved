# Generated by Django 4.0.9 on 2023-02-08 14:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_use_autofields_for_pk'),
        ('pods', '0002_pod_rule_pod_slot_pod_time_end_pod_time_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('label', models.TextField(blank=True, max_length=1024)),
                ('slot', models.DurationField(default=datetime.timedelta(seconds=1800))),
            ],
        ),
        migrations.RemoveField(
            model_name='pod',
            name='slot',
        ),
        migrations.AddField(
            model_name='pod',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pod',
            name='holidays',
            field=models.TextField(default='UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pod',
            name='rule',
            field=models.ForeignKey(blank=True, help_text='Default rule is a workdays only.', null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.rule'),
        ),
    ]
