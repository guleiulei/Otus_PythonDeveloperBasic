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
    users = []
    for user in await get_users():
        user_ = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'],)
        users.append(user_)
    return users


async def fetch_posts() -> List[Post]:
    posts = []
    for post in await get_posts():
        #post_ = Post(id=post['id'], user_id=post['user_id'], title=post['title'], body=post['body'])
        post_ = Post(id=post['id'], title=post['title'], body=post['body'])
        posts.append(post_)
    return posts


async def add_users():
    users, posts = await asyncio.gather(
        fetch_users(),
        fetch_posts(),
    )

async with Session() as session:
    async with session.begin():
        session.add_all(users + posts)


async def async_main():
    await create_tables()
    await add_users()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

