from django.conf.urls import url, include
from django.contrib import admin
from . import views # goi den class views de ke thua nhung def trong no
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #goi den ham about cua view
    url(r'^about$',views.about),

    #goi den homepage cua view, vi de no default la hien len nen moi viet laf "r'^$'"
    url(r'^$',views.homepage),

    # dung inclide la de goi den url cua app article, tu do co the truy cap vo cac page thuoc article
    url(r'^articles/',include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()