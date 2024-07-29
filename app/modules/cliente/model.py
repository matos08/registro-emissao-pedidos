from tortoise import Model
from tortoise import fields


class ClienteModel(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50)
    address = fields.CharField(max_length=50)
    telephone = fields.CharField(max_length=15)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "cliente"
        ordering = ["id"]
