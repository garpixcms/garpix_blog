from rest_framework.routers import DefaultRouter

from blog import viewset

router = DefaultRouter()
router.register('blog', viewset.BlogPageViewSet)
router.register('post', viewset.PostPageViewSet)
