import os
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr, relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Text

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, unique=True, primary_key=True)


class User(Base):
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)

    posts = relationship('Post', back_populates='user', uselist=True)


class Post(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)

    user = relationship('User', back_populates='posts', uselist=False)


Base = declarative_base(bind=async_engine, cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


def base():
    return None