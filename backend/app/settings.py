from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'garpix_blog',
]

GARPIX_BLOG_MIXIN = 'app.mixins.EmptyMixin'
GARPIX_BLOG_POST_MIXIN = 'app.mixins.EmptyMixin'
GARPIX_BLOG_POST_CATEGORY_MIXIN = 'app.mixins.EmptyMixin'
GARPIX_BLOG_POST_IMAGE_MIXIN = 'app.mixins.EmptyMixin'
GARPIX_BLOG_POST_VIDEO_MIXIN = 'app.mixins.EmptyMixin'

MIGRATION_MODULES.update(
    {'garpix_blog': 'app.migrations.garpix_blog'}
)