from django.db import models


class Subscribers(models.Model):
    email = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title_en = models.CharField(max_length=150, blank=False, null=False)
    title_ru = models.CharField(max_length=150, blank=True,null=True)
    title_uz = models.CharField(max_length=150, blank=False, null=False)
    description_en = models.TextField(blank=False, null=False)
    description_ru = models.TextField(blank=True, null=True)
    description_uz = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    full_name_en = models.CharField(max_length=150, blank=False, null=False)
    full_name_uz = models.CharField(max_length=150, blank=True, null=True)
    full_name_ru = models.CharField(max_length=150, blank=True, null=True)
    comment_en = models.TextField(blank=False, null=False)
    comment_uz = models.TextField(blank=True, null=True)
    comment_ru = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Advertising(models.Model):
    title_en = models.CharField(max_length=150, blank=True, null=True)
    title_uz = models.CharField(max_length=150, blank=True, null=True)
    title_ru = models.CharField(max_length=150, blank=True, null=True)
    comment_en = models.TextField(blank=True, null=True)
    comment_uz = models.TextField(blank=True, null=True)
    comment_ru = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to="image/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
