from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    groups = models.ManyToManyField(Group, related_name='marketplace_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='marketplace_user_permissions_set')

    def __str__(self):
        return self.username

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    school_class = models.CharField(max_length=50) # Example: "9th Grade", "High School"
    publisher = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="textbooks")
    description = models.TextField(blank=True) # Optional: Additional description
    condition = models.CharField(max_length=50, choices=[
        ('New', 'New'),
        ('Used - Excellent', 'Used - Excellent'),
        ('Used - Good', 'Used - Good'),
        ('Used - Fair', 'Used - Fair'),
    ], default='Used - Good')
    image = models.ImageField(upload_to='textbook_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    