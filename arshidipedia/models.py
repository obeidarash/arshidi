from django.db import models
import os
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, post_save
from management.models import Employee
from tinymce.models import HTMLField

CATEGORY = [
    ('web-development', 'Web Development'),
    ('seo', 'SEO'),
    ('wordpress', 'Wordpress'),
]


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_file_path(instance, filename):
    from time import time
    uid = str(uuid.uuid4().hex)[:10]
    name, ext = get_filename_ext(filename)
    time = str(time())
    final_name = f"{uid}{time[:10:-1]}{ext}"
    return f"arshidipedia/{final_name}"


class File(models.Model):
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to=upload_file_path)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE,
                                 help_text="This file belongs to whom?")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Library(models.Model):
    title = models.CharField(max_length=512)
    category = models.CharField(choices=CATEGORY, default=CATEGORY[0], max_length=128)
    file = models.FileField(upload_to=upload_file_path, null=True, blank=True,
                            help_text="Upload your pdf, docx, .... file in here")
    link = models.URLField(blank=True, null=True)
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Library"

    # Todo: Add Hashtag


# delete attach file after model has been deleted
@receiver(post_delete, sender=Library)
def post_save_expense(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


# update attach file after model has been updated
@receiver(pre_save, sender=Library)
def pre_save_expense(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).file.path
        try:
            new_img = instance.file.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


# delete attach file after model has been deleted
@receiver(post_delete, sender=File)
def post_save_expense(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


# update attach file after model has been updated
@receiver(pre_save, sender=File)
def pre_save_expense(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).attach.path
        try:
            new_img = instance.file.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
