from django.db import models

class contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    content=models.TextField(max_length=100)
    timestamp=models.DateTimeField()

    def __str__(self) :
        return "message from " + self.name +' - '+ self.email
    