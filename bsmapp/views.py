from django.shortcuts import render
from .models import SiteSettings, Hero, Client, FAQ, Service, Gallery, Blog, Uzmanlarimiz, About, SocialMedia

# Create your views here.

def index(request):
    context = {
        'site_settings': SiteSettings.objects.first(),
        'hero': Hero.objects.all(),
        'clients': Client.objects.all(),
        'services': Service.objects.all(),
        'gallery': Gallery.objects.all(),
        'blog': Blog.objects.all(),
        'uzmanlar': Uzmanlarimiz.objects.all(),
        'about': About.objects.first(),
        'faq': FAQ.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'clients': Client.objects.all(),
        'site_settings': SiteSettings.objects.first(),
        'about': About.objects.first(),
        'uzmanlar': Uzmanlarimiz.objects.all(),
        'services': Service.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'about.html', context)

def portfolio(request):
    context = {
        'gallery': Gallery.objects.all(),
        'site_settings': SiteSettings.objects.first(),
        'services': Service.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'portfolio.html', context)


def blog(request):
    context = {
        'blog': Blog.objects.all(),
        'site_settings': SiteSettings.objects.first(),
        'services': Service.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'blog.html', context)

def blog_single(request, pk):
    blog = Blog.objects.get(pk=pk)
    other_blogs = Blog.objects.exclude(pk=pk)
    context = {
        'blog': blog,
        'site_settings': SiteSettings.objects.first(),
        'services': Service.objects.all(),
        'blogs': other_blogs,
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'blog-single.html', context)

def contact(request):
    context = {
        'site_settings': SiteSettings.objects.first(),
        'faq': FAQ.objects.all(),
        'services': Service.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'contact.html', context)

def services(request):
    context = {
        'services': Service.objects.all(),
        'site_settings': SiteSettings.objects.first(),
        'faq': FAQ.objects.all(),
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'services.html', context)


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    other_services = Service.objects.exclude(pk=pk)
    social_media = SocialMedia.objects.all()
    context = {
        'service': service,
        'site_settings': SiteSettings.objects.first(),
        'services': other_services, 
        'social_media': social_media,
    }
    return render(request, 'services-detail.html', context)

