from datetime import datetime

from fastapi_camelcase import CamelModel

from app.modules.cliente import schemas


def test_cliente_schema(cliente_fake_dict):
    cliente = schemas.ClienteSchema(**cliente_fake_dict)
    assert isinstance(cliente, CamelModel)
    assert isinstance(cliente.id, int)
    assert isinstance(cliente.name, str)
    assert isinstance(cliente.email, str)
    assert isinstance(cliente.address, str)
    assert isinstance(cliente.telephone, str)
    assert isinstance(cliente.created_at, datetime)
    assert isinstance(cliente.updated_at, datetime)


def test_create_cliente_schema(cliente_fake_dict):
    cliente = schemas.CreateClienteSchema(**cliente_fake_dict)
    assert isinstance(cliente.name, str)
    assert isinstance(cliente.email, str)
    assert isinstance(cliente.address, str)
    assert isinstance(cliente.telephone, str)


def test_update_cliente_schema(cliente_fake_dict):
    cliente = schemas.UpdateClienteSchema(**cliente_fake_dict)
    assert isinstance(cliente.name, str)
    assert isinstance(cliente.email, str)
    assert isinstance(cliente.address, str)
    assert isinstance(cliente.telephone, str)
