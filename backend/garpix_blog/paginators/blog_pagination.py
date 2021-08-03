from rest_framework.pagination import PageNumberPagination, _positive_int
from collections import OrderedDict


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('num_pages', self.page.paginator.num_pages),
            ('num_current', self.page.number)
        ])

    def get_page_number(self, request, paginator):
        page_number = request.GET.get(self.page_query_param, 10)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                return _positive_int(
                    request.GET[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass
        return self.page_size
