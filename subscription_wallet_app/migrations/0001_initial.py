# Generated by Django 3.2.25 on 2024-05-06 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_email', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('receive_sms', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('renewal_frequency', models.CharField(max_length=50)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription_wallet_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription_wallet_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription_wallet_app.subscription')),
            ],
        ),
    ]
