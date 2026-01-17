import django.db.models as models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'courses'