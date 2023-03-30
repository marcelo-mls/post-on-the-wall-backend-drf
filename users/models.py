from django.db import models


class User(models.Model):
    name = models.CharField(max_length=45)
    initials = models.CharField(max_length=2)
    email = models.EmailField()
    encrypted_password = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.name}'
