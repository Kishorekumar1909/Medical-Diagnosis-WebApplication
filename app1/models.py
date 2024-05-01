from django.db import models

# Create your models here.
class patient(models.Model):

    Name = models.CharField(max_length = 200, null = True)
    DiseaseName = models.CharField(max_length = 200, null = True)
    Result = models.BooleanField()
    
    def __str__(self) -> str:
        return self.DiseaseName