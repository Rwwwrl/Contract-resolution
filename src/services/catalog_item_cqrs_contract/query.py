from attrs import define

from pydantic.types import PositiveFloat, PositiveInt

from src.framework.common.dto import DTO
from src.framework.cqrs.query import Query

__all__ = ('CatalogItemQuery', )


class CatalogItemDTO(DTO):

    price: PositiveFloat
    product_name: str


@define(frozen=True)
class CatalogItemQuery(Query[CatalogItemDTO]):

    id: PositiveInt
