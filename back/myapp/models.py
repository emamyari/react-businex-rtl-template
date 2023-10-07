from django.db import models


class gaming(models.Model):
    name = models.CharField(max_length=50)
    categori = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    class Meta:
        db_table = "myapp_gaming"


class maping(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = "myapp_maping"


class maping(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_maping"



