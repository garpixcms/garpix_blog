from polymorphic_tree.models import PolymorphicMPTTModel

from ..managers.polymorphic_active_manager import PolymorphicActiveManager


class PolymorphicActiveMixin(PolymorphicMPTTModel):
    active_objects = PolymorphicActiveManager()

    class Meta:
        abstract = True
