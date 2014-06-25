from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fragdev.views',

		# Handle all of the "static" pages
		url(r'^$', 'home', name='home'),
		url(r'^about/?$', 'about', name='about'),
		url(r'^contact/?$', 'contact', name='contact'),
		url(
			r'^contacted/?$',
			TemplateView.as_view(template_name="base-contacted.html"),
			name='contacted'
		),
		url(
			r'^projects/?$',
			TemplateView.as_view(template_name="base-projects.html"),
			name='projects'
		),
		url(
			r'^resume/?$',
			TemplateView.as_view(template_name="base-resume.html"),
			name='resume'
		),
		url(
			r'^services/?$',
			TemplateView.as_view(template_name="base-services.html"),
			name='services'
		),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Blog URLs
if 'wiblog' in settings.INSTALLED_APPS:
	urlpatterns += patterns('wiblog.views',
		url(r'^blog/', include('wiblog.urls', app_name='wiblog', namespace='wiblog')),
	)
