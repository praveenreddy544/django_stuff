from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasklist(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    managed_by_user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    '''def __str__(self):
        return self.task +" " + str(self.done)'''

    def __str__(self):
        return self.task + "with value"+ str(self.done)