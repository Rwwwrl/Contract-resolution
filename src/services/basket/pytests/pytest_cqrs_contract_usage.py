import attrs

from pydantic.types import PositiveInt

from src.services.catalog_item_cqrs_contract.query import CatalogItemDTO, CatalogItemQuery


class TestCatalogItemQuery:
    def test_query_contract(self):
        assert hasattr(attrs.fields(CatalogItemQuery), 'id')
        assert attrs.fields(CatalogItemQuery).id.type == PositiveInt

    def test_query_response_contract(self):
        response_type = CatalogItemQuery.__response_type__()

        assert response_type == CatalogItemDTO

        assert CatalogItemDTO.model_fields.get('price', None) is not None
        assert CatalogItemDTO.model_fields['price'].annotation == float
