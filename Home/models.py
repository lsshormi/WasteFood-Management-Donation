from django.db import models
from django.utils import timezone

# this is db is used for all donar list 😁
class DonateNow(models.Model):
    dname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    FoodT = models.CharField(max_length=122)
    FoodQ = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.IntegerField()
    date = models.DateField(default=timezone.now)

    
    class Meta:
        verbose_name_plural = 'DonateNows' 

    def __str__(self):
        return self.email

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nid = models.IntegerField()
    vemail = models.CharField(primary_key=True, max_length=122)
    password = models.CharField(max_length=122)
    vaddress = models.CharField(max_length=122)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=50)
    describe = models.TextField()
    date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Vlunteers'

    def __str__(self):
        return self.vemail
