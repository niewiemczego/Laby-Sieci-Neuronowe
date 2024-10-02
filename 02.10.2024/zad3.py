def get_result(n: list[int]) -> tuple[int, int, float] | None:
    if len(n) <= 0:
        return None

    max_value = max(n)
    min_value = min(n)
    avg = sum(n) / len(n)

    return max_value, min_value, avg


if __name__ == "__main__":
    import random

    random_values = random.sample(range(1, 100), 10)
    print(random_values)

    result = get_result(random_values)
    print(result)
