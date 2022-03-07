"""
Book: Building RESTful Python Web Services
"""
from django.db import models


class Breed(models.Model):
    T = 'Tiny'
    S = 'Small'
    M = 'Medium'
    L = 'Large'
    SIZE_CHOICES = (
        (T, 'Tiny'),
        (S, 'Small'),
        (M, 'Medium'),
        (L, 'Large'),        
    )
    ABILITY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=M)
    frnd = models.IntegerField(choices=ABILITY_CHOICES, default=1)
    train = models.IntegerField(choices=ABILITY_CHOICES, default=1)
    shed = models.IntegerField(choices=ABILITY_CHOICES, default=1)
    exercise = models.IntegerField(choices=ABILITY_CHOICES, default=1)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Dog(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(
        Breed, 
        related_name='dogs', 
        on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    color = models.CharField(max_length=200)
    favfood = models.CharField(max_length=200)
    favtoy = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
