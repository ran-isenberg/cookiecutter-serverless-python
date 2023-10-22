from functools import lru_cache

from {{cookiecutter.service_name}}.dal.db_handler import DalHandler
from {{cookiecutter.service_name}}.dal.dynamo_dal_handler import DynamoDalHandler


@lru_cache
def get_dal_handler(table_name: str) -> DalHandler:
    return DynamoDalHandler(table_name)
