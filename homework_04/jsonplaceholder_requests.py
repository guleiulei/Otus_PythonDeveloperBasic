from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users_data():
    async with ClientSession() as session:
        user_data = await fetch_json(session, USERS_DATA_URL)
    return user_data


async def fetch_posts_data():
    async with ClientSession() as session:
        post_data = await fetch_json(session, POSTS_DATA_URL)
    return post_data


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
