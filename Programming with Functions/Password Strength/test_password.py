from password import password_strength
import pytest 
from pytest import approx

def test_password_strength():
    assert password_strength("12345") == 0

pytest.main(["-v", "--tb=line", "test_password.py"])
