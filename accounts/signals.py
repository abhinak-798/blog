from django.db.models.signals import post_save
from accounts.models import CustumUser
from django.dispatch import receiver

@receiver(post_save,sender=CustumUser)
def show_message(sender,instance,created,**kwargs):
    if created:
        print("Welcome")