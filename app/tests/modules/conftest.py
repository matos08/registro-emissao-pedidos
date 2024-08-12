from datetime import datetime

from faker import Factory
import pytest

faker = Factory.create("pt_BR")


@pytest.fixture()
def pedidos_fake_dict():
    return {
        "id": faker.random_int(min=1, max=999),
        "status": faker.name(),
        "total_value": faker.pyfloat(min_value=1.0, max_value=999.9, right_digits=2),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "finished_at": datetime.now(),
    }


@pytest.fixture()
def create_pedidos_fake_dict():
    return {
        "status": faker.name(),
        "total_value": faker.pyfloat(min_value=1.0, max_value=999.9, right_digits=2),
        "cliente_id": 1,
    }


@pytest.fixture()
def cliente_fake_dict():
    return {
        "id": faker.random_int(min=1, max=999),
        "name": faker.name(),
        "email": faker.name(),
        "address": faker.name(),
        "telephone": faker.name(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }


@pytest.fixture()
def create_cliente_fake_dict():
    return {
        "name": faker.name(),
        "email": faker.name(),
        "address": faker.name(),
        "telephone": faker.name(),
    }
