from django.db import models

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='nome')
    url_link = models.CharField(null=True, max_length=255)
    url_img = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name: 'aula'
