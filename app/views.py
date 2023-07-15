from django.shortcuts import render, redirect
from app.form import ContactForm
from app.models import Skill, Blog, Contact


def index_view(request):
    skills = Skill.objects.all()
    blogs = Blog.objects.order_by('-id')[:2]

    return render(request=request,
                  template_name='app/index.html',
                  context={'skills': skills,
                           'blogs': blogs})


def all_blogs(request):
    blogs = Blog.objects.order_by('-id')

    return render(request=request,
                  template_name='app/all_blogs.html',
                  context={'blogs': blogs})


def article(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    return render(request=request,
                  template_name='app/article.html',
                  context={'blog': blog})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = ContactForm()

    return render(request=request,
                  template_name='app/index.html',
                  context={'form': form})