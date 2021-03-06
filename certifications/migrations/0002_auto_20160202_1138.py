# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 11:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificationprogramme',
            name='file',
        ),
        migrations.AddField(
            model_name='certificationprogramme',
            name='cert_template',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='certificationprogramme',
            name='certifiers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificationprogramme',
            name='description',
            field=models.TextField(default=datetime.datetime(2016, 2, 2, 11, 38, 1, 756360, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificationprogramme',
            name='expiery',
            field=models.PositiveSmallIntegerField(blank=True, help_text=b'in years', null=True),
        ),
        migrations.AddField(
            model_name='certificationprogramme',
            name='prerequisities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discipline',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discipline',
            name='linage',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='certificationprogramme',
            name='achivement',
            field=models.TextField(verbose_name=b'habilitations & Competences'),
        ),
        migrations.AlterField(
            model_name='certificationprogramme',
            name='authority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorities.Authority', verbose_name=b'released by'),
        ),
        migrations.AlterField(
            model_name='certificationprogramme',
            name='cert_type',
            field=models.PositiveSmallIntegerField(choices=[(1, b'Attendance'), (2, b'Diploma')]),
        ),
        migrations.AlterField(
            model_name='certificationprogramme',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cert_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificationprogramme',
            name='requires',
            field=models.ForeignKey(blank=True, help_text='indicates if other certification programe is necessary', null=True, on_delete=django.db.models.deletion.CASCADE, to='certifications.CertificationProgramme'),
        ),
    ]
