from django.db import models
from django.dispatch import receiver
import os
from .validator import validate_file_extension
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Department(models.Model):
    title = models.CharField(max_length=200,help_text="NAME OF DEPARTMENT")
    def __str__(self):
        return self.title



class Course(models.Model):

    title=models.CharField(max_length=200,help_text='NAME OF COURSE')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    description=models.TextField(blank=True,default=None)
    chapter_title = models.CharField(max_length=200,help_text='NAME OF CHAPTER/MODULE')
    # document = models.FileField(_("file"),upload_to='documents/',validators=[validate_file_extension],help_text="ONLY PDFS EXPECTED")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_title

class Material(models.Model):
    name = models.CharField(max_length=100,help_text="NAME TO PDF")
    document = models.FileField(_("file"), upload_to='documents/', validators=[validate_file_extension],
                                help_text="ONLY PDFS EXPECTED",blank=True,default=None)
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

@receiver(models.signals.post_delete, sender=Chapter)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Chapter` object is deleted.
    """
    if instance.document:
        if os.path.isfile(instance.document.path):
            os.remove(instance.document.path)

@receiver(models.signals.pre_save, sender=Chapter)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Chapter` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Chapter.objects.get(pk=instance.pk).document
    except Chapter.DoesNotExist:
        return False

    new_file = instance.document
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

