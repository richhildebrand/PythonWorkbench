from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    wordProblem = models.TextField()
    methodBody = models.TextField()

class MethodCall(models.Model):
    exercise = models.ForeignKey(Exercise)
    methodCall = models.TextField()
    expectedResult = models.CharField(max_length=100)