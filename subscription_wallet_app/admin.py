from django.contrib import admin
from .models import Category, User, Subscription, Payment
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Payment)