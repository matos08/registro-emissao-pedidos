from datetime import datetime

from fastapi_camelcase import CamelModel

from app.modules.pedidos import schemas


def test_pedidos_schema(pedidos_fake_dict):
    pedidos = schemas.PedidosSchema(**pedidos_fake_dict)
    assert isinstance(pedidos, CamelModel)
    assert isinstance(pedidos.id, int)
    assert isinstance(pedidos.status, str)
    assert isinstance(pedidos.total_value, float)
    assert isinstance(pedidos.created_at, datetime)
    assert isinstance(pedidos.updated_at, datetime)
    assert isinstance(pedidos.finished_at, datetime)


def test_create_pedidos_schema(pedidos_fake_dict):
    pedidos_fake_dict["cliente_id"] = 1
    pedidos = schemas.CreatePedidosSchema(**pedidos_fake_dict)
    assert isinstance(pedidos, CamelModel)
    assert isinstance(pedidos.status, str)
    assert isinstance(pedidos.total_value, float)


def test_update_pedidos_schema(pedidos_fake_dict):
    pedidos = schemas.UpdatePedidosSchema(**pedidos_fake_dict)
    assert isinstance(pedidos, CamelModel)
    assert isinstance(pedidos.status, str)
    assert isinstance(pedidos.total_value, float)
