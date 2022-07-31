from sorting_algorithms import merge


def main() -> None:
    iterable1 = [1, 2, 3]
    iterable2 = (2, 3, 4)
    iterator = merge(iterable1, iterable2)
    for item in iterator:
        print(item)


if __name__ == '__main__':
    main()
