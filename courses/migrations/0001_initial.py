# Generated by Django 3.1.5 on 2021-01-25 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('daily_play_time', models.IntegerField()),
                ('day', models.DateField(auto_now_add=True)),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
        ),
        migrations.AddIndex(
            model_name='registrations',
            index=models.Index(fields=['id_user'], name='idx_user'),
        ),
        migrations.AddIndex(
            model_name='registrations',
            index=models.Index(fields=['id_course'], name='idx_course'),
        ),
        migrations.AddIndex(
            model_name='progress',
            index=models.Index(fields=['id_course'], name='idx_course_progress'),
        ),
        migrations.AddIndex(
            model_name='progress',
            index=models.Index(fields=['day'], name='idx_day'),
        ),
    ]
