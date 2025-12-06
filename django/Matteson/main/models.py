from django.db import models
class bd(models.Model):
    title = models.CharField("naz",max_length=100)
    anons = models.CharField("anons",max_length=100)
    full = models.TextField("full")
    date = models.DateTimeField("date published")

    class Meta:
        verbose_name = "nowost"
        verbose_name_plural = "nowosti"

    def __str__(self):
        return self.title
# Create your models here.
