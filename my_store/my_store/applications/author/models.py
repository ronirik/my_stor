from django.db import models
# from django.forms import CharField


class Author(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    data_birth = models.DateField()
    place_birth = models.CharField(max_length=40)

    def __str__(self):
        return self.last_name