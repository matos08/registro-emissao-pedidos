from tortoise import Model
from tortoise import fields


class CorModel(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=50)
    value = fields.FloatField()

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "cor"
        ordering = ["id"]
