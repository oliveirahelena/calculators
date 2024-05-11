from .calculator_4 import Calculator4
from typing import Dict
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={{"numbers": [1, 2, 3, 4, 5]}})
    calculator_4 = Calculator4

    response = calculator_4.calculate(mock_request)

    assert "data" in response
    assert "data" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 3
    assert response["data"]["Calculator"] == 4


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_4 = Calculator4

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
