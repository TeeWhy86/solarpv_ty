from django.db import models


# Create your models here.
class Client(models.Model):
    clientCode = models.CharField(max_length=60, null=True)
    clientName = models.CharField(max_length=60)
    clientType = models.CharField(max_length=60)

    class Meta:
        ordering = ['clientName']

        def __str__(self):
            return self.clientName


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    state = models.CharField(max_length=60)
    postalcode = models.CharField(max_length=5)
    country = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=11, null=True)
    faxnumber = models.CharField(max_length=11, null=True)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class Product(models.Model):
    modelnum = models.CharField(primary_key=True, max_length=60)
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

    class Meta:
        ordering = ['modelnum']

        def __str__(self):
            return self.modelnum


class TestStandard(models.Model):
    standardid = models.AutoField(primary_key=True)
    standardname = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    publishdate = models.DateField()


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, null=False, unique=True)
    first = models.CharField(max_length=60, null=False)
    middle = models.CharField(max_length=60, null=True)
    last = models.CharField(max_length=60, null=False)
    job = models.CharField(max_length=60, null=True)
    email = models.EmailField(help_text='sample@gmail.com', null=True)
    office = models.CharField(max_length=60, help_text='Enter as XXX-XXX-XXXX', null=True)
    cell = models.CharField(max_length=60, help_text='Enter as XXX-XXX-XXXX', null=True)
    Dr = 'DR'
    Mr = 'MR'
    Ms = 'MS'
    Mrs = 'MRS'
    prefix_choices = [
        (Dr, 'Dr'),
        (Mr, 'Mr'),
        (Ms, 'Ms'),
        (Mrs, 'Mrs'),
    ]
    prefix = models.CharField(
        max_length=3,
        choices=prefix_choices,
        default=Dr,
    )
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    Yes = 'Y'
    No = 'N'
    staff_choices = [
        (Yes, 'Yes'),
        (No, 'No'),
    ]
    staff = models.CharField(
        max_length=3,
        choices=staff_choices,
        default=Yes,
    )
    # staff = models.TextChoices(choices=[''])


class Certificate(models.Model):
    certid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    reportnum = models.IntegerField()
    issuedate = models.DateField()
    standardid = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelnum = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['issuedate']

        def __str__(self):
            return self.certid


class TestSequence(models.Model):
    sequenceid = models.AutoField(primary_key=True)
    sequencename = models.CharField(max_length=60)

    class Meta:
        ordering = ['sequencename']


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
    fifrequency = models.CharField(max_length=60)
    standardid = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.serviceid
