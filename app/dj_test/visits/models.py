from django.db import models

class Visits(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Visits: {self.count}"

    class Meta:
        verbose_name_plural = "Visits"
