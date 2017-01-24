from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.title
