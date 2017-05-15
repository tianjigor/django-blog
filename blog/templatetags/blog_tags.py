from blog.models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_categories_count():
    return Category.objects.annotate(num_posts=Count('post'))


@register.simple_tag
def get_tag_count():
    return Tag.objects.annotate(num_posts=Count('post'))