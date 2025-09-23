# feedback/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductFeedback(models.Model):
    name = models.CharField(max_length=100)  # Reviewer's display name
    product_name = models.CharField(max_length=100)  # Product being reviewed
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # Rating 1-5
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product_name}"
