import pytest


def test_hello():
    assert "Hello, world!" == "Hello, world!"


def test_hello_world():
    """Very first test - basic assertion."""
    greeting = "Hello, World!"
    assert greeting == "Hello, World!", "Hello World test failed"
    print(greeting)


@pytest.mark.parametrize("name, expected", [
    ("Oracle QA Engineer", "Hello, Oracle QA Engineer!"),
    ("15 years experience", "Hello, 15 years experience!")
])
def test_hello_parametrized(name, expected):
    """Second basic test - using parameters."""
    greeting = f"Hello, {name}!"
    assert greeting == expected