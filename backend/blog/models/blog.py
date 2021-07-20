from garpix_page.models import BasePage


class BlogPage(BasePage):
    class Meta:
        verbose_name = "Список Новостей/Акций"
        verbose_name_plural = "Списки Новостей/Акций"
        ordering = ('-created_at',)
