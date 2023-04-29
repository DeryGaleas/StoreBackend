from strawberry_django_plus import gql
from Inventory.models import Inventory
from typing import Optional, List


@gql.django.type(Inventory)
class InventoryType(gql.Node):
    name: gql.auto
    creation_date: gql.auto
    cost: gql.auto
    current_stock: gql.auto


@gql.django.input(Inventory)
class CreateInventoryInput():
    name: gql.auto
    cost: gql.auto
    current_stock: gql.auto

@gql.django.input(Inventory)
class UpdateInventoryInput():
    name: gql.auto
    cost: gql.auto
    current_stock: gql.auto

