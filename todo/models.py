from django.db import models


class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(max_length=400)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

