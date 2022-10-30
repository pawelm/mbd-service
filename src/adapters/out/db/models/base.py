from sqlalchemy import MetaData
from sqlalchemy.orm import registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor
