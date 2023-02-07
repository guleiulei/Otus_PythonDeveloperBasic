import asyncio
from homework_04.jsonplaceholder_requests import get_posts, get_users
from homework_04.models import async_engine
from homework_04.models import User, Post, Base, Session
from typing import List


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_users() -> List[User]:
    users_data = []
    for user in await get_users():
        user_ = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
        users_data.append(user_)
    return users_data


async def fetch_posts() -> List[Post]:
    posts_data = []
    for post in await get_posts():
        if 'user_id' in post:
            post_ = Post(id=post['id'], user_id=post['user_id'], title=post['title'], body=post['body'])
            posts_data.append(post_)
    return posts_data


async def add_users():
    users_data, posts_data = await asyncio.gather(
        fetch_users(),
        fetch_posts(),
    )
    async with Session() as session:
        async with session.begin():
            session.add_all(users_data + posts_data)


async def async_main():
    await create_tables()
    await add_users()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

