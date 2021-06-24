from django.shortcuts import render

posts = [
    {
        'author': 'TsvetkovAA',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'June 22, 2021'
    },
    {
        'author': 'SinyavinDS',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'June 23, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
