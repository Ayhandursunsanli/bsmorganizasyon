from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class SiteSettings(models.Model):
    logo_img = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name='Logo Resmi')
    company_name = models.CharField(max_length=255, verbose_name='Şirket Adı')
    company_address = models.CharField(max_length=255, verbose_name='Şirket Adresi')
    google_maps_iframe = models.TextField(blank=True, null=True, verbose_name='Google Maps Embed Kodu')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Telefon')

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'

class Hero(models.Model):
    heroimg = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Hero Resmi')
    herotitle = models.CharField(max_length=255, verbose_name='Hero Başlığı')
    herodesc = models.TextField(verbose_name='Hero Açıklaması')
    heroahref = models.URLField(blank=True, null=True, verbose_name='Hero Linki')

    class Meta:
        verbose_name = 'Hero Bölümü'
        verbose_name_plural = 'Hero Bölümü'

    def __str__(self):
        return self.herotitle

class Client(models.Model):
    clientslogoimg = models.ImageField(upload_to='clients/', blank=True, null=True, verbose_name='Müşteri Logo Resmi')

    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteriler'

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='Soru')
    answer = models.TextField(verbose_name='Cevap')

    class Meta:
        verbose_name = 'Sıkça Sorulan Sorular'
        verbose_name_plural = 'Sıkça Sorulan Sorular'

    def __str__(self):
        return self.question

class Service(models.Model):
    img = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Hizmet Resmi')
    title = models.CharField(max_length=255, verbose_name='Hizmet Başlığı')
    desc = RichTextField(verbose_name='Hizmet Açıklaması')
    anasayfa = models.BooleanField(default=False, verbose_name='Anasayfada Görünsün mü?')

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name='Galeri Başlığı')
    img = models.ImageField(upload_to='gallery/', blank=True, null=True, verbose_name='Galeri Resmi')

    class Meta:
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeriler'

    def __str__(self):
        return self.title

class Blog(models.Model):
    author = models.CharField(max_length=255, verbose_name='Yazar')
    date = models.DateField(verbose_name='Tarih')
    img = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name='Blog Resmi')
    title = models.CharField(max_length=255, verbose_name='Blog Başlığı')
    desc = RichTextField(verbose_name='Blog Açıklaması')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return self.title

class Uzmanlarimiz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Uzmanın Adı')
    img = models.ImageField(upload_to='uzmanlar/', blank=True, null=True, verbose_name='Uzmanın Resmi')
    job = models.CharField(max_length=255, verbose_name='Uzmanın Mesleği')
    
    class Meta:
        verbose_name = 'Uzman'
        verbose_name_plural = 'Uzmanlar'

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Hakkımızda Başlığı')
    desc = RichTextField(null=True, blank=True, verbose_name='Hakkımızda Açıklaması')
    desc2 = RichTextField(null=True, blank=True, verbose_name='Hakkımızda Açıklaması 2')
    
    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızda'

    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    name = models.CharField(max_length=255, verbose_name='Sosyal Medya Adı')
    url = models.URLField(verbose_name='Sosyal Medya Linki')
    icon = models.CharField(max_length=255, verbose_name='Sosyal Medya İkonu')

    class Meta:
        verbose_name = 'Sosyal Medya'
        verbose_name_plural = 'Sosyal Medya'
    
    def __str__(self):
        return self.name

