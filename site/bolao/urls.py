#coding:utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from usuarios.views import CadastroUsuario
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bolao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cadastro/$', CadastroUsuario.as_view()),
    url(r'^embreve/$', TemplateView.as_view(template_name="embreve.html")),
	url(r'^$', TemplateView.as_view(template_name="index.html")),

)

# Serve a mídia estática enquanto está em DEBUG
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    )
