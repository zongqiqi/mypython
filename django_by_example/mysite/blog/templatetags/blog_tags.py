from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

register=template.Library()

from ..models import Post

import markdown


"""
simple_tag:处理数据并返回一个字符串（string）
inclusion_tag：处理数据并返回一个渲染过的模板（template）
assignmeng_tag：处理数据并在上下文（context）中设置一个变量（variable）


"""

@register.simple_tag
def total_posts():
	return Post.published.count()


#使用包含标签，返回上下文变量用来渲染模板
#展示最新的五条博客信息
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts=Post.published.order_by('-publish')[:count]
	return {'latest_posts':latest_posts}


#分配模板标签（类似简单标签，但是将结果存储在给予的变量中）
#展示拥有最多评论的帖子
@register.assignment_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comments=Count('comments')).order_by(
													'-total_comments')[:count]


@register.filter(name='markdown')#过滤器名称命名为markdown
def markdowm_format(text):#防止函数名与模块名冲突，函数名定义为markdown_ormat
	return mark_safe(markdown.markdown(text))