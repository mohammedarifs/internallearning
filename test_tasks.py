import pytest
pytestmark = [pytest.mark.P2 , pytest.mark.tasks]

@pytest.mark.task1
def test_task1():
    print("login pass")

@pytest.mark.P2
@pytest.mark.tasks
@pytest.mark.task2
def test_task2():
    print("login pass")