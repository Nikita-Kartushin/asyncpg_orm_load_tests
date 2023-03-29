from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "tortoise_a" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "tac_int" INT NOT NULL,
    "tac_str" TEXT NOT NULL,
    "tac_date_time" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "tortoise_b" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "tbc_str" TEXT NOT NULL,
    "tbc_fk_ta_id" BIGINT NOT NULL REFERENCES "tortoise_a" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "tortoise_c" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "tcc_str" TEXT NOT NULL,
    "tbc_fk_ta_id" BIGINT NOT NULL REFERENCES "tortoise_b" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "tortoise_d" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "tcc_str" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "tortoise_d_tortoise_a" (
    "tortoise_d_id" BIGINT NOT NULL REFERENCES "tortoise_d" ("id") ON DELETE CASCADE,
    "tortoise_a_id" BIGINT NOT NULL REFERENCES "tortoise_a" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
