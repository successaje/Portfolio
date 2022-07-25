from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import uuid


class Project(models.Model):
    title = models.CharField(max_length = 250)
    thumbnail = models.ImageField(null = True)
    body = RichTextField()
    slug = models.SlugField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True,  editable = False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True,  editable = False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length = 250, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique =True, primary_key = True, editable = False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    body = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.body[0:50]

class Message(models.Model):
    name = models.CharField(max_length = 250, null = True)
    email = models.CharField(max_length = 250, null = True)
    subject = models.CharField(max_length = 250, null = True)
    body = models.TextField()
    is_read = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return self.name

class Endorsement(models.Model):
    name = models.CharField(max_length = 200, null = True)
    body = models.TextField()
    approved = models.BooleanField(default = False, null = True)
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.body[0:50]


class Question(models.Model):

    TYPES = (
        ("backend", "backend"),
        ("frontend", "frontend"),
        ("fullstack", "fullstack"),
    )

    answer = models.CharField(max_length = 250, choices = TYPES)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return self.answer
        
        