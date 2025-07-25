from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
