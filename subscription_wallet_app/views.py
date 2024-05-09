from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import generic
from .models import Subscription

# Create your views here.

class index_view(TemplateView):
    template_name = 'index.html'

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

# You can add more views here for creating, updating, and deleting subscriptions if needed
