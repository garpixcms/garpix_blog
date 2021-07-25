from polymorphic_tree.models import PolymorphicMPTTModel

from garpix_blog.managers import PolymorphicActiveManager


class PolymorphicActiveMixin(PolymorphicMPTTModel):
    active_objects = PolymorphicActiveManager()

    class Meta:
        abstract = True
