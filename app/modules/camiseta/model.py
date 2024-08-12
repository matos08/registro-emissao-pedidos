from tortoise import Model
from tortoise import fields


class CamisetaModel(Model):
    id = fields.BigIntField(pk=True)
    size_shirt = fields.CharField(max_length=50)
    type_cloth = fields.CharField(max_length=50)
    type_shirt = fields.CharField(max_length=50)
    color_cloth = fields.CharField(max_length=50)
    quantity = fields.IntField(default=1)

    orcamento = fields.ForeignKeyField(
        model_name="models.OrcamentoModel",
        related_name="camiseta",
        null=True
    )

    pintura = fields.ManyToManyField(model_name="models.PinturaModel",
                                     through="pintura_camiseta",
                                     related_name="camiseta"
                                     )

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "camiseta"
        ordering = ["id"]
