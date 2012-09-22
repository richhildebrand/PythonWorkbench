from django.contrib import admin
from Exercise.models import Exercise, MethodCall

class MethodCallDisplay(admin.TabularInline):
	model = MethodCall
	extra = 4

class ExerciseAdminDisplay(admin.ModelAdmin):
	inlines = [MethodCallDisplay]

admin.site.register(Exercise, ExerciseAdminDisplay)