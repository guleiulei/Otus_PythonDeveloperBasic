import asyncio
from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import async_engine
from homework_04.models import User, Post, Base, Session, async_session
from typing import List


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(users_data):
    users_list = []
    for user in users_data:
        user = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
        users_list.append(user)
    async with async_session() as session:
        async with session.begin():
            session.add_all(users_list)


async def create_posts(posts_data):
    posts_list = []
    for post in posts_data:
        post = Post(id=post['id'], title=post['title'], user_id=post['userId'], body=post['body'])
        posts_list.append(post)
    async with async_session() as session:
        async with session.begin():
            session.add_all(posts_list)




async def add_users():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    async with Session() as session:
        async with session.begin():
            session.add_all(users_data + posts_data)


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(fetch_users_data(), fetch_posts_data())
    await create_tables()
    await create_users(users_data)
    await create_posts(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
