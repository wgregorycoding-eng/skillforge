from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Mastered', 'Mastered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='skills')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('Article', 'Article'),
        ('Video', 'Video'),
        ('Course', 'Course'),
        ('Book', 'Book'),
    ]

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='Article')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.resource_type})"


class StudySession(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    reflection_notes = models.TextField()

    def __str__(self):
        return f"Study session for {self.skill.title} on {self.date} ({self.duration_minutes} mins)"