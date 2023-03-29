TORTOISE_ORM = {
    "connections": {"default": "asyncpg://test:test@localhost:5436/tortoise_db"},
    "apps": {
        "models": {
            "models": ["tortoise_client.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}