from django.db import models

class Sample(models.Model):
    Food_ID = models.CharField(max_length=200)
    UPC = models.CharField(max_length=200)
    Product_Name = models.CharField(max_length=200)
    Food_Group = models.CharField(max_length=200)
    Calories = models.DecimalField(max_digits=20, decimal_places=5)
    Total_Carbohydrates = models.DecimalField(max_digits=20, decimal_places=5)
    Protein = models.DecimalField(max_digits=20, decimal_places=5)
    Total_Fat = models.DecimalField(max_digits=20, decimal_places=5)
    Sodium = models.DecimalField(max_digits=20, decimal_places=5)
    Cholesterol = models.DecimalField(max_digits=20, decimal_places=5)
    Sugars = models.DecimalField(max_digits=20, decimal_places=5)
    # main field / key
    def __str__(self):
        return self.Food_ID

