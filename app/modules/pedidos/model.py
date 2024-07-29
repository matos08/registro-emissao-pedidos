from tortoise import Model
from tortoise import fields


class PedidosModel(Model):
    id = fields.BigIntField(pk=True)
    status = fields.CharField(max_length=50)
    total_value = fields.CharField(max_length=50)
    cliente = fields.ForeignKeyField(
        "models.ClienteModel",
        "pedidos",
    )

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    finished_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "pedidos"
        ordering = ["id"]
