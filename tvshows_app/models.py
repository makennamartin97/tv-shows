from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Show name should be at least 2 characters!"
        if len(postData['network']) < 4:
            errors['network'] = "Network should be at least 3 characters!"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters!"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


# Create your models here.
