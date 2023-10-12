def fn(inp):
    arr = [i for i in range(1, inp + 1)]

    for i in range(inp - 2):
        new_vals = get_next_triplet(arr[i : i + 3])
        arr[i] = new_vals[0]
        arr[i + 1] = new_vals[1]
        arr[i + 2] = new_vals[2]

    return arr


def get_next_triplet(sub_arr):
    if sub_arr[2] <= sub_arr[1]:
        sub_arr[2] = sub_arr[1] + 1

    while not condition(sub_arr):
        is_factor = (sub_arr[0] + sub_arr[1]) % 3 == 0
        if is_factor:
            sub_arr[1] += 1

        sub_arr[2] += 1

    return sub_arr


def condition(arr):
    return len(arr) == len(set(arr)) and ((3 * arr[2]) % sum(arr[:2])) != 0


def main():
    tests = int(input())

    for _ in range(tests):
        print(" ".join(map(str, fn(int(input())))))


if __name__ == "__main__":
    main()
