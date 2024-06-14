from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from typing_extensions import OrderedDict


class Pagination(LimitOffsetPagination):
    default_limit = 100

    def get_paginated_response(self, data, data_totalizer=None):
        data_result = OrderedDict([
            ('count', self.count),
            ('limit', self.limit),
            ('offset', self.offset),
            ('results', data)
        ])
        if data_totalizer is not None:
            data_result.update(data_totalizer)
        return Response(data_result)
