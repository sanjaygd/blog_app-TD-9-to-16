from django.shortcuts import render

from .models import Post

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,'blog_app/post_list.html',context)
