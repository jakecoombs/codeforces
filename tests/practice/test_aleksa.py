import pytest

from practice.aleksa import condition, fn


@pytest.mark.parametrize(
    "input",
    [[1, 3, 5], [6, 8, 12]],
)
def test_condition(input) -> None:
    assert condition(input)


@pytest.mark.parametrize(
    "input",
    [i for i in range(3, 10)],
)
def test_script(input) -> None:
    result = fn(input)

    for i in range(input - 2):
        newArr = result[i : (i + 3)]
        assert condition(newArr)
