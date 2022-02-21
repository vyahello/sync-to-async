import time


def sleep(n: int) -> None:
    time.sleep(3)
    print(f'finished {n} iteration')


def main() -> None:
    for n in range(10):  # type: int
        sleep(n)


if __name__ == '__main__':
    main()
