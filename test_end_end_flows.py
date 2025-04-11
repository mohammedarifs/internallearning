import pytest
pytestmark = [pytest.mark.P3 , pytest.mark.end_to_end_flows]

@pytest.mark.sql_to_azure
def test_sql_azure():
    print("login pass")

@pytest.mark.nas_to_azure
def test_nas_Azuere():
    print("login pass")