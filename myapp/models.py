from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Group(models.Model):
    name = models.CharField( max_length=50)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self) -> str:
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.TextField(max_length=60)

