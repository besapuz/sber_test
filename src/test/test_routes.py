from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/deposit",
        json={
                "date": "25.03.2023",
                "periods": 5,
                "amount": 3000000,
                "rate": 8
            }
    )
    assert response.status_code == 200
    assert response.json() == {
                                "25.04.2023": 3020000,
                                "25.05.2023": 3040133.33,
                                "25.06.2023": 3060400.89,
                                "25.07.2023": 3080803.56,
                                "25.08.2023": 3101342.25
                                }

