from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
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

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
