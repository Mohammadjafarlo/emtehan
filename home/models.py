from django.db import models


class meno_veladat(models.Model):
    title = models.CharField(max_length=200)
    esm_namayeshy = models.CharField(max_length=200)

class meno_shahadat(models.Model):
    title = models.CharField(max_length=200)
    esm_namayeshy = models.CharField(max_length=200)
class madahy1(models.Model):
    daste = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    matn = models.TextField()
    file = models.FileField(upload_to='' )



