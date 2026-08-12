from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):

    CATEGORY_CHOICES = [
        ('github', 'GitHub'),
        ('youtube', 'YouTube'),
        ('documentation', 'Documentation'),
        ('article', 'Article'),
        ('leetcode', 'LeetCode'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='links'
    )

    title = models.CharField(max_length=200)

    url = models.URLField()

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    is_favourite = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


from django.contrib import admin
from .models import Link



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'user',
        'is_favourite',
        'created_at',
    )

    list_filter = (
        'category',
        'is_favourite',
    )

    search_fields = (
        'title',
        'description',
        'url',
    )