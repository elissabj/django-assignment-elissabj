from django.db import models
"""
views.CompanyViewSet)
router.register(r'movies', views.MoviesViewSet)
router.register(r'', views.DisneyCompanyViewSet)
"""

class Company(models.Model):
    name = models.CharField(max_length=128)

class Movie(models.Model):
    name = models.CharField(max_length=256)
    publish_year = models.SmallIntegerField()
    hours = models.DateTimeField(null=True, hrs = True)
    companies = models.ManyToManyField(Company, through='DisneyCompany')

class DisneyCompany(models.Model):
    movie = models.ForeignKey(Movie, related_name='MoviesWithCompany', on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, related_name='CompanyWithMovies', on_delete=models.DO_NOTHING)