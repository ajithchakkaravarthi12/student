from django.db import models # type: ignore

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.mobile} - {self.city}"
