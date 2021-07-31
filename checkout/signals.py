# sends signals
from django.db.models.signals import post_save, post_delete
# recieves signals
from django.dispatch import receiver
# where the signals come from
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Parameters ref to the sender of the signal
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print('delete signal recieved!')
    instance.order.update_total()