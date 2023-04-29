import strawberry
from typing import List
from Inventory.api.mutation import Mutation
from Inventory.api.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)