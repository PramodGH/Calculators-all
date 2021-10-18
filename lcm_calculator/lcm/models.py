from django.db import models
# from django.utils.timezone.now

# model
class lcm_db(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=1000)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    date_modified = models.DateTimeField(auto_now_add=True)