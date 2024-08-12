from fastapi import status


def test_health_check_should_be_return_200(test_app):
    response = test_app.get("/health-check")
    assert response.status_code == status.HTTP_200_OK
