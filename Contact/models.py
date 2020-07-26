from django.db import models

# Create your models here.
class Contact(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255,blank=False)
    Email = models.EmailField(max_length=254)
    Message = models.TextField(max_length=5000)
    User_Ip = models.GenericIPAddressField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    class Meta:
        db_table = "Contact Us"
