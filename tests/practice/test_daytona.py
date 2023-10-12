import pytest

from practice.daytona import is_commmon_in_subseg


@pytest.mark.parametrize(
    ["n", "k", "arr", "expected"],
    [(5, 4, [1, 4, 3, 4, 1], True), (4, 1, [2, 3, 4, 4], False)],
)
def test_is_common_subseg(
    n: int, k: int, arr: list[int], expected: bool
) -> None:
    assert is_commmon_in_subseg(n, k, arr) == expected
