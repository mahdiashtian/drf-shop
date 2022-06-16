import os
GALLERY_IMAGE_ROOT = 'products/gallery/'


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_galleries_image_path(instance=None,filename=None):
    name,ext = get_file_name(filename)
    final_name = f"{instance.title}{ext}"
    return f"{GALLERY_IMAGE_ROOT}{instance.id}/{final_name}"