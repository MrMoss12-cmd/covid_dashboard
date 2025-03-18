from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'

class CovidData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    confirmed_cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    active_cases = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']
        unique_together = ['country', 'date']

    def __str__(self):
        return f"{self.country.name} - {self.date}"

class VaccinationData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    total_vaccinations = models.IntegerField(default=0)
    people_vaccinated = models.IntegerField(default=0)
    people_fully_vaccinated = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']
        unique_together = ['country', 'date']

    def __str__(self):
        return f"{self.country.name} - {self.date}"