from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

DEFAULT_IMG_URL = "mountains.jpeg"

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.fullname()

class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.CharField(max_length=50, default=DEFAULT_IMG_URL)
    date = models.DateField(auto_now = True)
    slug = slug = models.SlugField(
                        default="",
                        unique=True,
                        null=False,
                        blank=True,
                        )
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
                    Author,
                    on_delete=models.SET_NULL,
                    related_name="posts",
                    null=True,
                    )
    tags = models.ManyToManyField(Tag,
                    related_name="posts"
                    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

