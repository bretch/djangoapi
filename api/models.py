from django.db import models
from jsonfield import JSONField

class Person(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def phone_number_default():
        return []
    def email_address_default():
        return []        
    def address_default():
        return []                

    phoneNumbers = JSONField("PhoneNumber", default=phone_number_default)
    emailAddresses = JSONField("EmailAddress", default=email_address_default)
    addresses = JSONField("Address", default=address_default)

    def __str__(self):
        return "{}".format(self.name)