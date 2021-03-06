from django.db import models
from django.contrib.auth import get_user_model


# Paper implementation containing all the paper fields
class Paper(models.Model):
    paperID = models.IntegerField(default=0)
    title = models.CharField(max_length=50)

    # Author is a foreign key so field has to be filled by a author object.
    author = models.ManyToManyField(get_user_model())

    date = models.DateTimeField('date published')
    abstract = models.TextField(default=' ', max_length=500)
    BibTex = models.TextField(default=' ', max_length=200)
    PaperPDF = models.FileField(default=' ')
    PeerPDF = models.FileField(default=' ')

    # string function that returns the paper title when this class is printed.
    def __str__(self):
        return self.title