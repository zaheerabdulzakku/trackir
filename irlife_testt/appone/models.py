from django.db import models
from django.urls import reverse
# Create your models here.

class IrList(models.Model):
    RFC_STAT = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    irno=models.PositiveIntegerField(primary_key=True)
    rfc=models.CharField(max_length=1,choices=RFC_STAT)

    def get_absolute_url(self):
        return reverse("appone:detail",kwargs={'pk':self.pk})
