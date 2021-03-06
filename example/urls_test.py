from django.conf.urls import include, url
from rest_framework import routers

from example.views import BlogViewSet, EntryViewSet, AuthorViewSet
from .api.resources.identity import Identity, GenericIdentity

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'blogs', BlogViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'authors', AuthorViewSet)

# for the old tests
router.register(r'identities', Identity)

urlpatterns = [
    url(r'^', include(router.urls)),

    # old tests
    url(r'identities/default/(?P<pk>\d+)',
        GenericIdentity.as_view(), name='user-default'),
]

