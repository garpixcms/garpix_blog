from rest_framework.routers import DefaultRouter

from garpix_blog import viewset

router = DefaultRouter()
router.register('blog', viewset.BlogPageViewSet)
router.register('post', viewset.PostPageViewSet)
