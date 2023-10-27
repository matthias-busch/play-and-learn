import pytest
from unittest.mock import Mock
import pytest_tutorial_freecodecamp.service as service
from pytest_mock import MockerFixture
import requests

def test_get_user_from_db(mocker: MockerFixture) -> None:
    mocker.patch(
        "pytest_tutorial_freecodecamp.service.get_user_from_db",
        return_value="Mocked Alice"
    )

    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"


def test_get_users(mocker: MockerFixture) -> None:
    mock_response = {
        "id": 1,
        "name": "John Doe"
    }

    mocker.patch(
        "requests.get",
        return_value=Mock(json=lambda: mock_response, status_code=200)
    )

    users = service.get_users()

    assert users["id"] == 1
    assert users["name"] == "John Doe"

def test_get_users_error(mocker: MockerFixture) -> None:
    mocker.patch(
        "requests.get",
        return_value=Mock(status_code=400)
    )

    with pytest.raises(requests.HTTPError):
        service.get_users()
