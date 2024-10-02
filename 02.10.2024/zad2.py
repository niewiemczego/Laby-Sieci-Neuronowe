def main(a: float, b: float, c: float) -> tuple[float, float] | float | None:
    delta = b**2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        return (-b - delta**0.5) / (2 * a), (-b + delta**0.5) / (2 * a)


if __name__ == "__main__":
    print(main(1, 2, 1))
    print(main(1, 2, 3))
    print(main(1, 3, 2))
    print(main(1, 1, 1))
    print(main(1, 0, 0))
