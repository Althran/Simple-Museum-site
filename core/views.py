from django.shortcuts import render, get_object_or_404
from .models import Post, Item, Contest
from django.views.generic import TemplateView


def contest_list(request):
    contests = Contest.objects.all()
    return render(request, 'contest.html', {'contests': contests})


def item_list(request):
    items = Item.objects.all()
    return render(request, 'eksponaty.html', {'items': items})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detail.html', {'post': post})


class ContextMixin:
    context = {

    }


class StandsTemplateView(ContextMixin, TemplateView):
    template_name = 'stands.html'

    def get_context_data(self, **kwargs):
        context = super(StandsTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class ContactTemplateView(ContextMixin, TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data()
        context.update(self.context)
        return context
