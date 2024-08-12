from tortoise import Model
from tortoise import fields


class PinturaModel(Model):
    id = fields.BigIntField(pk=True)
    img_url = fields.CharField(max_length=50)
    size_painting = fields.IntField()
    value_colors = fields.FloatField()

    orcamento = fields.ForeignKeyField(
        model_name="models.OrcamentoModel",
        related_name="pintura",
        null=True
    )

    cor = fields.ManyToManyField(model_name="models.CorModel",
                                 through="cor_pintura",
                                 related_name="pintura"
                                 )

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "pintura"
        ordering = ["id"]
