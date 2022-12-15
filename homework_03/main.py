"""
Инструкция:
1. Открыть проект через виртуальное окружение
2. В терминале запустите контейнер -> docker run -it -p 8000:8000 app
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_root():
    return {
        "message": "pong",
    }
