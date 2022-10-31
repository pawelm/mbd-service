from enum import unique

from passlib.context import CryptContext
from sqlalchemy import Column, Integer, Unicode, UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, synonym

from .base import Base
from utils import hash_password


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=512), nullable=False, unique=True)
    _password = Column("password", Unicode(length=512), nullable=False)
    posts = relationship("Post")

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = hash_password(value)

    password = synonym("_password", descriptor=password)

    def __unicode__(self):
        return f"User {self.name}"
