from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Todo

from django.core.mail import send_mail


@receiver(post_save, sender=Todo)
def todo_post_save_action(*args, **kwargs):
    if kwargs.get('created'):
        obj = kwargs.get('instance')
        subject = 'New Todo Created'
        msg = obj.notes
        receivers = ['youssef.ibrahem.2022@gmail.com']
        send_mail(subject=subject, message=msg, from_email='youssef.15404@gmail.com', recipient_list=receivers)