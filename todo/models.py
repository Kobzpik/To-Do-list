from django.db import models

# Create your models here.
# here are create the database and link the database

class list1(models.Model):
    date= models.DateField(max_length=20)
    item= models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed) 

   
        