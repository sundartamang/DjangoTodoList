from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False, verbose_name='Is completed ?', null=True, blank=True)

    def __str__(self):
        return self.title