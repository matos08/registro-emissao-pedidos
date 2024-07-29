from tortoise import Model
from tortoise import fields


class PinturaModel(Model):
    id = fields.BigIntField(pk=True)
    img_url = fields.CharField(max_length=50)
    size_painting = fields.IntField
    value_colors = fields.FloatField

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "pintura"
        ordering = ["id"]
