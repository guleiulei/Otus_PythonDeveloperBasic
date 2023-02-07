from aiohttp import ClientSession


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users():
    async with ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.json()
            return html


async def get_posts():
    async with ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.json()
            return html