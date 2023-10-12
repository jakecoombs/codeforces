def is_commmon_in_subseg(n, k, arr):
    return k in arr


def main():
    tests = int(input())

    for _ in range(tests):
        n, k = map(int, input().split(" "))
        arr = map(int, input().split(" "))
        print("YES") if is_commmon_in_subseg(n, k, arr) else print("NO")


if __name__ == "__main__":
    main()
