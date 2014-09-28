from django.conf.urls.defaults import *
from mysite.views import *
from mysite.books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    #
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^$', home),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^http/$', test_http),
    (r'search-form/$', views.search_form),
    (r'search/$', views.search),
)
