from polymorphic.managers import PolymorphicManager


class PolymorphicActiveManager(PolymorphicManager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_active=False)
