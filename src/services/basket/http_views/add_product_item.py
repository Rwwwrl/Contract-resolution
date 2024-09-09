from pydantic.types import PositiveInt

from src.framework.common.dto import DTO
from src.mywebframework.response import Response
from src.services.catalog_item_cqrs_contract.query import CatalogItemQuery

__all__ = ('add_product_item', )


class RequestData(DTO):
    product_id: PositiveInt


def add_product_item(request_data: RequestData) -> Response:
    ...
    catalog_item = CatalogItemQuery(id=request_data.product_id).fetch()
    # от результата запроса CatalogItemQuery нам нужен ТОЛЬКО атрибут price
    # дальше мы его как-то используем
    price = catalog_item.price    # noqa
    ...
    return Response(content='', status=200)
