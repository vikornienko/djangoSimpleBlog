
# from django.http import Http404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


from .models import Post
from .forms import EmailPostForm

# Create your views here.

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read"\
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\s comments: {cd['comments']}"
            send_mail(subject, message, 'your_account@ex.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'appblog/post/share.html', {'post': post, 'form': form, 'sent': sent})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'appblog/post/list.html'

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "appblog/post/list.html", {"posts": posts})

def post_detail(request, post, year, month, day):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish_at__year=year,
                             publish_at__month=month,
                             publish_at__day=day)

    return render(request, "appblog/post/detail.html", {"post": post})

