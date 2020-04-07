from django.db import models


# Create your models here.
class Client(models.Model):
    # clientCode = models.CharField(max_length=60)
    clientName = models.CharField(max_length=60)
    clientType = models.CharField(max_length=60)


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    postalcode = models.CharField(max_length=5)
    country = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=11)
    faxnumber = models.CharField(max_length=11)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class Product(models.Model):
    modelnum = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    celltechnology = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=60)
    totalcells = models.IntegerField
    cellsinseries = models.IntegerField()
    seriesstrings = models.IntegerField()
    bypassdiodes = models.IntegerField()
    length = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()
    supertype = models.CharField(max_length=60)
    supermanufacturer = models.CharField(max_length=60)
    subtype = models.CharField(max_length=60)
    submanufacturer = models.CharField(max_length=60)
    frametype = models.CharField(max_length=60)
    frameadhesive = models.CharField(max_length=60)
    encaptype = models.CharField(max_length=60)
    encapmanufacturer = models.CharField(max_length=60)
    junctype = models.CharField(max_length=60)
    juncmanufacturer = models.CharField(max_length=60)


class TestStandard(models.Model):
    standardid = models.AutoField(primary_key=True)
    standardname = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    publishdate = models.DateField()


class User(models.Model):
    # username = models.CharField(max_length=60)
    # password = models.CharField(max_length=60)
    userid = models.AutoField(primary_key=True)
    first = models.CharField(max_length=60)
    middle = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    job = models.CharField(max_length=60)
    email = models.EmailField()
    office = models.CharField(max_length=60)
    cell = models.CharField(max_length=60)
    prefix = models.CharField(max_length=60)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    # staff = models.CharField(max_length=60)


class Certificate(models.Model):
    certid = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    reportnum = models.IntegerField()
    issuedate = models.DateField()
    standardid = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelnum = models.ForeignKey(Product, on_delete=models.CASCADE)


class TestSequence(models.Model):
    sequenceid = models.AutoField(primary_key=True)
    sequencename = models.CharField(max_length=60)


class Performance(models.Model):
    modelnum = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequenceid = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    maxvolt = models.IntegerField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()


class Service(models.Model):
    serviceid = models.AutoField(primary_key=True)
    servicename = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    firequired = models.BooleanField()
    fifequency = models.CharField(max_length=60)
    standardid = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
