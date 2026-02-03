import django.db.models as models


class Degree(models.Model):
    name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'degrees'
