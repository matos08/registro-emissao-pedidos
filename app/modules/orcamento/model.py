from tortoise import Model
from tortoise import fields


class OrcamentoModel(Model):
    id = fields.BigIntField(pk=True)
    service = fields.CharField(max_length=50)
    value = fields.FloatField()
    descount = fields.FloatField()

    pedidos = fields.ForeignKeyField(
        model_name="models.PedidosModel",
        related_name="orcamento",
        null=True
    )

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "orcamento"
        ordering = ["id"]
