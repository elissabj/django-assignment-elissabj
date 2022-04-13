from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=128)
    verte_type = models.CharField(max_length=128)
    vital_function = models.CharField(max_length=128)
    

class Environment(models.Model):
    name_enviro = models.CharField(max_length=256)
    wildlife = models.CharField(max_length=256)
    descrip_enviro= models.CharField(max_length=256)
    enviros = models.ManyToManyField(Animal, through='AnimalEnvi')


class AnimalEnvi (models.Model):
    animal = models.ForeignKey(Animal, related_name='AnimalEnviron', on_delete=models.DO_NOTHING)
    environment = models.ForeignKey(Environment, related_name='EnvrionAnimal', on_delete=models.DO_NOTHING)
    def __str__(self):
    	return f'{self.id}'

