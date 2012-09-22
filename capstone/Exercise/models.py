from django.db import models

class Exercise(models.Model):
	def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50)
    wordProblem = models.TextField()
    methodBody = models.CharField(max_length=250)

class MethodCall(models.Model):
    exercise = models.ForeignKey(Exercise)
    methodCall = models.CharField(max_length=250)
    expectedResult = models.CharField(max_length=100)