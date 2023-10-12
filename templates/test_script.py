import pytest


@pytest.mark.parametrize(
    ["input", "expected"],
    [(False, True)],
)
def test_script(input, expected) -> None:
    assert input == expected
