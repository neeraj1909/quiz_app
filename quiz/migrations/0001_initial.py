# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name="Answer's text")),
                ('is_valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Exam name')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=256, verbose_name="Question's text")),
                ('is_published', models.BooleanField(default=False)),
                ('answers', models.ManyToManyField(to='quiz.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
    ]