from django.db import models

# Create your models here.
class student(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null= False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')

    item = (('JUNIOR', 'Junior'), ('SENIOR', 'Senior'))
    cYears_in_school = models.CharField(max_length=10, choices=item)

    def __str__(self):
        return self.cName