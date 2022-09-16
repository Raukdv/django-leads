from django.urls import path, include, re_path

from panel import views

urlpatterns = [
    path(
        'leads/',
        include(('lead.urls', 'lead'), namespace='lead')
    ),
    path(
        'site/',
        include(('core.urls', 'site'), namespace='site')
    ),
]

urlpatterns += [
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
]