from django.conf.urls.defaults import *
from mysite.views import *
from mysite.books import views
from mysite.contacts.views import *
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
    (r'^view1/$', view_1),
    (r'^view2/$', view_2),



    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^http/$', test_http),
    (r'search-form/$', views.search_form),
    (r'search/$', views.search),

    (r'contact/$', contact),
    (r'thanks/$', thanks),
)
