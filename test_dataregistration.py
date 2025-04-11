import pytest

pytestmark = [pytest.mark.P1 , pytest.mark.dataregistration]


@pytest.mark.physical
def test_Physical_dataregistration():
    print("login pass")

@pytest.mark.virtual
def test_virtaul_dataregistration():
    print("login pass")
