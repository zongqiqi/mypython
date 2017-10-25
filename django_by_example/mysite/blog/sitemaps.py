from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
	changefreq='weekly'#帖子页面的修改频率
	priority=0.9#帖子在网站中的关联性（最大1）
	def items(self):#返回站点地图所包含对象的查询集
		return Post.published.all()
	def lastmod(self,obj):#接收items返回的每一个对象，并返回对象的最后修改时间
		return obj.publish