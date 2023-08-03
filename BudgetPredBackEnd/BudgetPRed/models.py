from django.db import models
from rest_framework import serializers # Importing serializers

# Create your models here.

class Budget(models.Model):

    #id 
    IDEIMPST = models.IntegerField(primary_key=True, default=0 )
    MONTSTRU = models.FloatField()
    MONTRAPP = models.FloatField()
    MOISSOLD = models.DateField( default='2021-01-01')
    CODTYPAC = models.CharField(max_length=3, default='AA')
    LIBACTGE = models.CharField(max_length=50, default='no libelle')
    Budgets = models.FloatField()
    
    # String representation of the model
    def __str__(self):
        return str(self.IDEIMPST) + ' ' + str(self.LIBACTGE)
    
    # create method to create a new budget
    def create(self, validated_data):
        return Budget.objects.create(**validated_data)
    
    # update method to update an existing budget
    def update(self, instance, validated_data):
        instance.IDEIMPST = validated_data.get('IDEIMPST', instance.IDEIMPST)
        instance.MONTSTRU = validated_data.get('MONTSTRU', instance.MONTSTRU)
        instance.MONTRAPP = validated_data.get('MONTRAPP', instance.MONTRAPP)
        instance.MOISSOLD = validated_data.get('MOISSOLD', instance.MOISSOLD)
        instance.CODTYPAC = validated_data.get('CODTYPAC', instance.CODTYPAC)
        instance.LIBACTGE = validated_data.get('LIBACTGE', instance.LIBACTGE)
        instance.Budgets = validated_data.get('Budgets', instance.Budgets)
        instance.save()
        return instance
    
class User(models.Model):
    id = models.IntegerField(primary_key=True, default=0 )
    username = models.CharField(max_length=50, default='no username')
    email = models.CharField(max_length=50, default='no email')
    password = models.CharField(max_length=50, default='no password')
    # String representation of the model
    def __str__(self):
        return str(self.id) + ' ' + str(self.username) + ' ' + str(self.email) + ' ' + str(self.password)
    
    # create method to create a new user
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    # update method to update an existing user
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
