TORTOISE_ORM = {
    "connections": {"default": "asyncpg://test:test@localhost:5436/tortoise_db"},
    "apps": {
        "models": {
            "models": ["tortoise.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}