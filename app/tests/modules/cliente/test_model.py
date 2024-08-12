from datetime import datetime

from tortoise import Model

from app.modules.cliente.model import ClienteModel


def test_cliente_model(cliente_fake_dict):
    cliente = ClienteModel(**cliente_fake_dict)
    assert isinstance(cliente, Model)
    assert isinstance(cliente.id, int)
    assert isinstance(cliente.name, str)
    assert isinstance(cliente.email, str)
    assert isinstance(cliente.address, str)
    assert isinstance(cliente.telephone, str)
    assert isinstance(cliente.created_at, datetime)
    assert isinstance(cliente.updated_at, datetime)
