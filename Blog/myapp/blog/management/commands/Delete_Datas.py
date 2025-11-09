from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Post.objects.all().delete()

        self.stdout.write(self.style.WARNING("Deleting Data Successfully Completed"))
    