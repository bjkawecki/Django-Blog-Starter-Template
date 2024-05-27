from django.core.management import BaseCommand, CommandError

from blog.models.post import Post
from blog.models.tag import Tag
from blog.models.source import Source



class Command(BaseCommand):
    help = "Carefull. Removes all posts, tags, sources from the database."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--number", dest="number", default=5,
            help="Specifies the password for the superuser.",
        )

    def handle(self, *args, **options):
        confirm = input("This will delete all posts, tags and sources from the database.\nAre you sure? (y/N)\n")
        if confirm == "y":
            Post.objects.all().delete()
            Tag.objects.all().delete()
            Source.objects.all().delete()
            print("Successfully deleted all posts, tags and sources.")
        else:
            print("Deletion aborted.")