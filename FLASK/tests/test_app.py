import pytest
from app import *

# content of test_app.py
@pytest.hello.world
def test_hello_world():
    assert hello_world() == 'Hello World!'