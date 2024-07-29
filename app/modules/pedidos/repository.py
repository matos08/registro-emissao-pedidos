from app.modules.pedidos.model import PedidosModel


class PedidoRepository:
    """
    Class responsible for performing actions on the database
    """

    def __init__(self):
        self.entity = PedidosModel

    async def create(self, data: dict):
        return await self.entity.create(**data)

    async def get_or_none(self, **kwargs):
        """
        Objective to filter the first item found in the database
        :param kwargs: Attributes followed by key and value
        exemple: id = 1
        :return:
        """
        return await self.entity.filter(**kwargs).first()

    async def delete(self, **kwargs):
        """
        Objective to delete the items found in the database
        :param kwargs: Attributes followed by key and value
        exemple: id = 1
        :return:
        """
        await self.entity.filter(**kwargs).delete()
        return True

    async def update(self, _id: int, **kwargs):
        """
        Objective to update the items found in the database
        :param _id: id of object inside the database
        :param kwargs: Attributes followed by key and value
        exemple:name= test
        :return:
        """
        await self.entity.filter(id=_id).update(**kwargs)
        return await self.get_or_none(id=_id)
