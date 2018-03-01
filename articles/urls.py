from django.conf.urls import url
from . import views # goi den class views de ke thua nhung def trong no

urlpatterns = [
#   "r'^$'" nhu the nay thi khi mo app article default se show ra article list
    url(r'^$',views.article_list,name="list"),
    url(r'^/(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
]

