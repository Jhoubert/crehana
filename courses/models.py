from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64)


class Registrations(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['id_user'], name='idx_user'),
            models.Index(fields=['id_course'], name='idx_course')
        ]


class Progress(models.Model):
    id = models.AutoField(primary_key=True)
    daily_play_time = models.IntegerField()
    id_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    day = models.DateField(null=False, auto_now_add=True, blank=True)

    class Meta:
        indexes = [
                    models.Index(fields=['id_course'], name='idx_course_progress'),
                    models.Index(fields=['day'], name='idx_day')
        ]
