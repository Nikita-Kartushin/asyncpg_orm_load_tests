from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


meta_data = Base.metadata
