class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_possible(self) -> bool:
        init = [self.a, self.b, self.c]
        max_value = max(init)

        return sum(init) - max_value > max_value

    def get_type(self) -> str:
        if not self.is_possible():
            return "niemozliwy"

        if self.a**2 + self.b**2 > self.c**2:
            return "ostrokatny"
        elif self.a**2 + self.b**2 == self.c**2:
            return "prostokatny"
        else:
            return "rozwartokatny"


if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    print(t.is_possible())
    print(t.get_type())

    t = Triangle(3, 4, 10)
    print(t.is_possible())
    print(t.get_type())

    t = Triangle(3, 4, 7)
    print(t.is_possible())
    print(t.get_type())
