import factory
import random
from factory.faker import faker
from django.core.files.uploadedfile import SimpleUploadedFile


from .models.post import Post
from .models.tag import Tag
from .models.source import Source

FAKE = faker.Faker()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ('name',)

    name = "History"

    
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5)
    subtitle = factory.Faker("sentence", nb_words=12)
    teaser = factory.Faker("sentence", nb_words=36)
    slug = factory.Faker("slug")


    @factory.lazy_attribute
    def text(self):
        faker_text = ""
        for _ in range(0, 5):
            faker_text += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return faker_text

    published = True

    tag = factory.SubFactory(TagFactory)

    image = SimpleUploadedFile(name="test_image.jpg", content=open("blog/static/img/test_image.jpg", "rb").read(), content_type="image/jpeg")



class SourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Source

    hyperlink = factory.Faker("uri")
    name = factory.Faker("company")
    post = factory.SubFactory(PostFactory)
