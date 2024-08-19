import pytest
from src.domain.value_objects.username import Username


def test_valid_username():
    username = Username("valid_username")
    assert username.value == "valid_username"


def test_invalid_username_is_empty():
    with pytest.raises(ValueError) as exception_info:
        Username("")

    assert str(exception_info.value) == "Username cannot be empty or whitespace"


def test_invalid_username_is_whitespace():
    with pytest.raises(ValueError) as exception_info:
        Username(" ")

    assert str(exception_info.value) == "Username cannot be empty or whitespace"


def test_invalid_username_is_not_string():
    with pytest.raises(ValueError) as exception_info:
        Username(1)

    assert str(exception_info.value) == "Username must be a string"
