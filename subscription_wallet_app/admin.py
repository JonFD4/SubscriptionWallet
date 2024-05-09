from django.contrib import admin
from django.utils.html import format_html
from django.utils import formats
from .models import Category, User, Subscription, Payment

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_display', 'renewal_frequency', 'discount_display', 'payment_button')
    list_filter = ('renewal_frequency', 'category')
    search_fields = ('name', 'category__name', 'user__django_user__username')
    date_hierarchy = 'start_date'

    def discount_display(self, obj):
        return obj.discount if obj.discount else '-'
    discount_display.short_description = 'Discount'

    def price_display(self, obj):
        return formats.currency(obj.price)
    price_display.short_description = 'Price'

    def payment_button(self, obj):
        price = formats.currency(obj.price)
        discount = formats.currency(obj.discount) if obj.discount else '-'
        total = formats.currency(obj.price - obj.discount) if obj.discount else formats.currency(obj.price)
        payment_info = f"Price: {price}"
        if obj.discount:
            payment_info += f", Discount: {discount}, Total: {total}"
        return format_html('<button type="button" onclick="window.location.href=\'/make_payment/{}/{}/\'">Pay</button>', obj.pk, obj.price)
    payment_button.short_description = 'Payment'

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user.userprofile
        super().save_model(request, obj, form, change)

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Payment)
