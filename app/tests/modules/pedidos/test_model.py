from datetime import datetime

from tortoise import Model

from app.modules.pedidos.model import PedidosModel


def test_pedidos_model(pedidos_fake_dict):
    pedidos = PedidosModel(**pedidos_fake_dict)
    assert isinstance(pedidos, Model)
    assert isinstance(pedidos.id, int)
    assert isinstance(pedidos.status, str)
    assert isinstance(pedidos.total_value, float)
    assert isinstance(pedidos.created_at, datetime)
    assert isinstance(pedidos.updated_at, datetime)
    assert isinstance(pedidos.finished_at, datetime)
