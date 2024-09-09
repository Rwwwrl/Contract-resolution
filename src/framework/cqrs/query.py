from typing import Generic, Type, TypeVar, _GenericAlias as GenericType

QueryResponseType = TypeVar('QueryResponseType')


class Query(Generic[QueryResponseType]):
    def fetch(self) -> QueryResponseType:
        ...

    @classmethod
    def __response_type__(cls) -> Type[QueryResponseType]:
        for base in cls.__orig_bases__:
            if type(base) is GenericType and base.__args__:
                return base.__args__[0]
