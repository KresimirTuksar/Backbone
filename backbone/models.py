from django.db import models
from django.db.models import Sum
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Tvrtka(models.Model):
    naziv = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.naziv


class Zaposlenik(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='zaposlenik')
    poslodavac = models.ForeignKey(Tvrtka, on_delete=models.CASCADE)
    

class Mjesto(models.Model):
    naziv = models.CharField(max_length=50, blank=True, null=True)
    kreirao = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.naziv
    

class Podrucje(models.Model):
    naziv = models.CharField(max_length=100, blank=True, null=True)
    dc = CharField(max_length=5, blank=True, verbose_name='DČ', null=True)
    mjesto = models.ForeignKey(Mjesto, null=True, related_name='podrucja', on_delete=models.CASCADE)
    kreirao = models.ForeignKey(User, null=True, related_name='podrucja', on_delete=models.CASCADE)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)
    je_uvezeno = models.BooleanField(default=False)
    
    def __str__(self):
        return self.naziv

    def ukupno_metara(self):
        return Dionica.objects.filter(podrucje=self).aggregate(Sum('duzina'))

    def ukupno_segmenata(self):
        return Kabel.objects.filter(dionica__podrucje=self).count()

    def od_toga_rijeseno(self):
        return Kabel.objects.filter(dionica__podrucje=self).filter(rijeseno = True).count()

    def postotak(self):
        if Kabel.objects.filter(dionica__podrucje=self).count() == 0:
            return int(0)
        else:
            return int((Kabel.objects.filter(dionica__podrucje=self).filter(rijeseno = True).count() / Kabel.objects.filter(dionica__podrucje=self).count())*100)
 

class Dionica(models.Model):
    rb = models.IntegerField(default=0,verbose_name='Redni broj', blank=True, null=True)
    naziv = models.CharField(max_length=50, null=True)
    podrucje = models.ForeignKey(Podrucje, null=True, related_name='dionice', on_delete=models.CASCADE)
    duzina = models.IntegerField(default=0, null=True, verbose_name='Dužina(m)', blank=True)
    kreirao = models.ForeignKey(User, null=True, related_name='dionice', on_delete=models.CASCADE)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.naziv)


class Odk(models.Model):
    naziv = models.CharField(max_length=50)
    podrucje = models.ForeignKey(Podrucje,related_name='odks', blank=True, null=True, on_delete=models.CASCADE)
    izvodjac = models.ForeignKey(Tvrtka, blank=True, null=True, on_delete=models.CASCADE)
    kreirao = models.ForeignKey(User, related_name='odks', null=True, on_delete=models.CASCADE)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.naziv

    """ def ukupno_metara(self):
        return Odk.objects.filter(odk=self).aggregate(Sum('duzina')) """

    def ukupno_segmenata(self):
        return Kabel.objects.filter(odk=self).count()

    def od_toga_rijeseno(self):
        return Kabel.objects.filter(odk=self).filter(rijeseno = True).count()

    def postotak(self):
        if Kabel.objects.filter(odk=self).count() == 0:
            return int(0)
        else:
            return int((Kabel.objects.filter(odk=self).filter(rijeseno = True).count() / Kabel.objects.filter(odk=self).count())*100)


   
class Kabel(models.Model):
    RIJESENO = 'Riješeno'
    ZASTOJ = 'Zastoj'
    IZVODENJE = 'U izvođenju'
    STATUS_CHOICES = (
        (RIJESENO,'Riješeno'),
        (ZASTOJ,'Zastoj'),
        (IZVODENJE,'U izvođenju'),
    )
    
    segment = models.CharField(max_length=10, blank=True)
    dionica = models.ForeignKey(Dionica, null=True,related_name='kablovi', on_delete=models.CASCADE)
    odk = models.ForeignKey(Odk, null=True, related_name='kablovi', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=IZVODENJE)
    pocetna = models.IntegerField(default=0, blank=True)
    zavrsna = models.IntegerField(default=0, blank=True)
    radna_duzina = models.IntegerField(default=0, blank=True)
    broj_niti = models.IntegerField(default=0, blank=True, null=True)
    napomena = models.CharField(max_length=100, blank=True, null=True)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)
    zadnje_azuriranje = models.DateTimeField(auto_now=True, auto_now_add=False)
    kreirao = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    azurirao = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    zavrseno_datum = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    zavrsio = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    rijeseno = models.BooleanField(default=False)

    def __str__(self):
        return self.segment

    
class Biljeska(models.Model):
    sadrzaj = models.CharField(max_length=2000, blank=True, null=False, verbose_name='Bilješka')
    kabel = models.ForeignKey(Kabel, related_name='biljeske', on_delete=models.CASCADE)
    kreirao = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    kreirano = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering = ['-kreirano'] # zadnja biljeska na vrh

    def __str__(self):
        return self.sadrzaj

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)