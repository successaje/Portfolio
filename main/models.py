from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length = 250)
    #thumbnail = models.ImageField()
    body = models.TextField()
    slug = models.SlugField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True,  editable = False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
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

        