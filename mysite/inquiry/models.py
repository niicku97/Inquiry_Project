from django.db import models

class InquiryClass(models.Model):
    type_cargo = (
        ('Livestock','Livestock'),
        ('Grains','Grains'),
        ('Cereal','Cereal')
    )
    type_container = (
        ('Refrigerated','Refrigerated'),
        ('Basic','Basic')
    )
    
    full_name = models.CharField(max_length=150)
    email     = models.EmailField()
    cargo     = models.CharField(max_length = 10, choices = type_cargo, default = 'Livestock')
    container = models.CharField(max_length = 13, choices = type_container, default = 'Refrigerated')

    objects = models.Manager()

    def __str__(self):
        return self.full_name

    

