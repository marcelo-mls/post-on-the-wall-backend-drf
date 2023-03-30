from django.db import models
from users.models import User


class Post(models.Model):
    post = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - ({self.user.name}) {self.post}'
