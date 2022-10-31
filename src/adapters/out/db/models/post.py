from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship

from .base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(length=100), nullable=False)
    content = Column(Unicode(length=1000), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    author_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    author = relationship("User", back_populates="posts")

    def __unicode__(self):
        return f"Post {self.title}"
