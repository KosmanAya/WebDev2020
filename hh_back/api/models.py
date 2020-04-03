from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'Companies'


    def __str__(self):
        return '{}. {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }

    def __str__(self):
        return self.name