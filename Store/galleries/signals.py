from django.dispatch import receiver
from django.db.models.signals import post_delete
import os


@receiver(post_delete,sender="galleries.Gallery")
def run_after_delete(instance,**kwargs):

    path = instance.image.path

    if os.path.exists(path):
        os.remove(path)
