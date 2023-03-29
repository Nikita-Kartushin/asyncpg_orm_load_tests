from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey


class Base(DeclarativeBase):
    pass


meta_data = Base.metadata


class SqlAlchemy_A(Base):
    __tablename__ = 'a'

    id = Column(Integer, primary_key=True)
    sac_int = Column(Integer)
    sac_str = Column(String)
    sac_date_time = Column(DateTime)
    sd_many = relationship('SqlAlchemy_D', secondary='da')


class SqlAlchemy_B(Base):
    __tablename__ = 'b'

    id = Column(Integer, primary_key=True)
    sbc_int = Column(Integer)
    sbc_fk_sa = Column(ForeignKey('a.id'))


class SqlAlchemy_C(Base):
    __tablename__ = 'c'

    id = Column(Integer, primary_key=True)
    sbc_str = Column(String)
    sbc_fk_sb = Column(ForeignKey('b.id'))


class SqlAlchemy_D(Base):
    __tablename__ = 'd'

    id = Column(Integer, primary_key=True)
    sbc_str = Column(String)

    sa_many = relationship('SqlAlchemy_A', secondary='da')


class SqlAlchemy_DA(Base):
    __tablename__ = 'da'

    sc_fk_sa = Column(ForeignKey('a.id'), primary_key=True)
    sc_fk_sd = Column(ForeignKey('d.id'), primary_key=True)
