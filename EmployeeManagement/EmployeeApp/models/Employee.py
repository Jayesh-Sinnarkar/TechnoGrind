from django.db import models

class Employee(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_hired = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
