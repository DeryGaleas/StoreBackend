from strawberry_django_plus import gql
from Inventory.models import Inventory
from .types import InventoryType, CreateInventoryInput, UpdateInventoryInput

@gql.type
class Mutation:
    create_model: InventoryType = gql.django.create_mutation(CreateInventoryInput)
    update_model: InventoryType = gql.django.update_mutation(UpdateInventoryInput)
    delete_model: InventoryType = gql.django.delete_mutation(gql.NodeInput)