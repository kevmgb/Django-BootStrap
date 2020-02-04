from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Each class is a table in the database (eg. Post)
# Each attribute is a field in the database (eg title) 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete post if user is deleted

    def __str__(self):
        return(self.title)

