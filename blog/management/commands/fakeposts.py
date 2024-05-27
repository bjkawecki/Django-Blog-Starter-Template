from django.core.management import BaseCommand, CommandError

from blog.factory import PostFactory, SourceFactory

from blog.models.post import Post
from blog.models.tag import Tag
from blog.models.source import Source

class Command(BaseCommand):
    help = "Create a bunch of fake blog posts."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--number",
            dest="number",
            default=5,
            help="Specifies the number of new fake blog posts to be generated.",
        )

    def handle(self, *args, **options):
        confirm = input("This will delete all posts, tags and sources from the database and create 5 new fake posts.\nAre you sure? (y/N)\n")
        if confirm == "y":
            number = int(options.get("number"))
            Post.objects.all().delete()
            Tag.objects.all().delete()
            Source.objects.all().delete()
            SourceFactory.create_batch(number)
            print("Success.")
        else:
            print("Aborted.")
        
