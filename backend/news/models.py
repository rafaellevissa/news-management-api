from django.db import models
from django.conf import settings
from django.utils import timezone

class Vertical(models.TextChoices):
    PODER = 'poder', 'Poder'
    TRIBUTOS = 'tributos', 'Tributos'
    SAUDE = 'saude', 'Saúde'
    ENERGIA = 'energia', 'Energia'
    TRABALHISTA = 'trabalhista', 'Trabalhista'

class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicada'),
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    vertical = models.CharField(max_length=20, choices=Vertical.choices)
    is_pro_only = models.BooleanField(default=False)
    scheduled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

