from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.views.generic import TemplateView
from django.views import generic
from .models import Subscription
from .models import user
from .forms import YourSignUpForm


# Create your views here.

class index_view(TemplateView):
    template_name = 'index.html'

# Creating user instance and adding user to database
def signup(request):
    if request.method=='POST':
        form = YourSignUpForm(request.post)
        if form is_valid():
            username= form.cleaned_data('username')
            email = form.cleaned_data('email')
            



@login_required
def dashboard(request):
    #Get user subscriptions
    user = request.user 
    user_subscriptions = Subscription.objects.filter(user=user)

    subscription_data =[]
    for subscription in user_subscriptions:
        subscriptions_info.append({
            'name': subscription.name,
            'next_payment_date': subscription.next_payment_date
        })
    context = {
        'subscriptions_info': subscriptions_info
    }
    return render(request, 'dashboard.html', context)


@login_required
def subscription_list(request):
    # Get subscriptions for the current user
    subscriptions = Subscription.objects.filter(user__django_user=request.user)

    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscription_list.html', context)

@login_required
def subscription_detail(request, subscription_id):
    # Get the subscription for the current user
    subscription = get_object_or_404(Subscription, id=subscription_id, user__django_user=request.user)

    context = {
        'subscription': subscription
    }
    return render(request, 'subscription_detail.html', context)
