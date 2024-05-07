from django.db import models
from django.contrib.auth.models import User as DjangoUser
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    django_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    receive_email = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    receive_sms = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.django_user.username

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    payment_date = models.DateField()
    start_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_frequency = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.amount} - {self.subscription.name}"
