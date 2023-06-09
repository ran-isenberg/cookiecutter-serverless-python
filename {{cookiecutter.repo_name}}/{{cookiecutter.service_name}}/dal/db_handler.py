from abc import ABC, abstractmethod

from {{cookiecutter.service_name}}.dal.schemas.db import OrderEntry


class DalHandler(ABC):

    @abstractmethod
    def create_order_in_db(self, customer_name: str, order_item_count: int) -> OrderEntry:
        ...  # pragma: no cover
