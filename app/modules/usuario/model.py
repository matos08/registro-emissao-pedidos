from tortoise import Model
from tortoise import fields


class UsuarioModel(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50)
    password = fields.CharField(max_length=50)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "usuario"
        ordering = ["id"]
