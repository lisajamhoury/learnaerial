from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^schools/new-york$', views.schools, name='schools'),
    url(r'^venues/new-york$', views.venues, name='venues'),
    url(r'^companies$', views.companies, name='companies'),
    url(r'^equipment$', views.equipment, name='equipment'),
    url(r'^newsletter_signup$', views.newsletter_signup, name='newsletter_signup'),
    url(r'^faq$', views.faq, name='faq')
]
