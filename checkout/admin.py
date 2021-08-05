from django.contrib import admin
from .models import Order, OrderLineItem

"""
inline item admin below allows us to add and edit line items in the admin
from inside the order model
"""
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # add inlines option here to add it to the order admin interface
    inlines = (OrderLineItemAdminInline,)
    # calc by model methods
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')
    # establishes the order of the fields which would otherwise be adjusted by django
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',  'original_bag',
              'stripe_pid')
    # only a few key items to display
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # reverse chronological order displayed so most recent at the top
    ordering = ('-date',) 
#registers Order and Order Admin models but skip inlone as its now accessible in the order model
admin.site.register(Order, OrderAdmin)