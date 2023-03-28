from tortoise import fields
from tortoise import Model


class BaseModel(Model):
    id = fields.BigIntField(pk=True)

    class Meta:
        abstract = True


class Tortoise_A(BaseModel):
    tac_int = fields.IntField()
    tac_str = fields.TextField()
    tac_date_time = fields.DatetimeField()


class Tortoise_B(BaseModel):
    tbc_str = fields.TextField()
    tbc_fk_ta = fields.ForeignKeyField(
        'models.Tortoise_A',
        related_name='tbc',
        on_delete=fields.SET_NULL
    )


class Tortoise_C(BaseModel):
    tcc_str = fields.TextField()
    tbc_fk_ta = fields.ForeignKeyField(
        'models.Tortoise_B',
        related_name='tbc',
        on_delete=fields.SET_NULL
    )


class Tortoise_D(BaseModel):
    tcc_str = fields.TextField()

    tbc_fk_ta = fields.ManyToManyField(
        'models.Tortoise_A',
        related_name='tbc',
        on_delete=fields.SET_NULL
    )
