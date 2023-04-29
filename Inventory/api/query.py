from strawberry_django_plus import gql
from Inventory.models import Inventory
from .types import InventoryType, CreateInventoryInput, UpdateInventoryInput
from typing import List
@gql.type
class Query:
    items : List[InventoryType] = gql.django.field()
    @gql.field
    def hello() -> str:
        return "hello"