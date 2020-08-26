from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Não Publicado'),
        ('published', 'Publicado'),
    )
    title = models.CharField('Titulo', max_length=250)
    slug = models.SlugField('Atalho', max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Autor')
    body = models.TextField('Texto')
    publish = models.DateTimeField('Publicação', default=timezone.now)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    update = models.DateTimeField('Atualizado em', auto_now_add=True)
    status = models.CharField('Status da postagem', max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('blog:post_detail',
                   args=[self.publish.year,
                         self.publish.month,
                         self.publish.day, self.slug])
