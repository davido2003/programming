from django.db import models
# Create your models here.
class ProgrammingNewsApi(models.Model):
    title = models.CharField(max_length=100)
    def nameFile(instance, filename):
        return '/'.join(['videos',str(instance.name), filename])
    video = models.FileField(upload_to='namefile',blank=True)
    link = models.URLField(max_length=200)
    


    def __str__(self) :
        return self.title
