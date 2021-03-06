# Generated by Django 3.2.7 on 2021-10-14 08:14

from django.db import migrations, models
import django.utils.timezone
import jutil.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', jutil.modelfields.SafeCharField(db_index=True, max_length=64, verbose_name='name')),
                ('task_id', jutil.modelfields.SafeCharField(db_index=True, max_length=64, verbose_name='task')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='last modified')),
                ('signal', jutil.modelfields.SafeCharField(db_index=True, max_length=64, verbose_name='signal')),
                ('executing', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='executing')),
                ('complete', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='complete')),
                ('locked', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='locked')),
                ('scheduled', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='scheduled')),
                ('retrying', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='retrying')),
                ('canceled', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='canceled')),
                ('revoked', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='revoked')),
                ('failed', models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='failed')),
                ('error', jutil.modelfields.SafeTextField(blank=True, verbose_name='error')),
            ],
            options={
                'verbose_name': 'background task',
                'verbose_name_plural': 'background tasks',
            },
        ),
    ]
