from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save
import os
from .models import Ip


@receiver(post_delete,sender="products.Product")
def run_after_delete(instance,**kwargs):
    
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)

    instance.ip.delete()


@receiver(pre_save,sender="products.Product")
def run_after_Save(instance,**kwargs):
    if not instance.ip:
        instance.ip = Ip.objects.create(id=instance.id,title=instance.title)