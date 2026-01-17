import django.db.models as models

'''

Course model for storing course information.

degree_programs is a JSONField that contains a list of dictionaries like below,
[
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]

'''

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20, unique=True)
    degree_programs = models.JSONField(default=list)

    class Meta:
        db_table = 'courses'