def fibonacci_series(n):
    if n < 0:
        raise ValueError("Number cannot be negative")

    series = []

    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series