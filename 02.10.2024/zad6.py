class Rectangle:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b
        self.area = 0

    def calculate_area(self) -> None:
        self.area = self.a * self.b

    @classmethod
    def load(cls) -> "Rectangle | None":
        try:
            a = float(input("Podaj a: "))
            b = float(input("Podaj b: "))
        except ValueError:
            print("Podano zle dane!")
            return None

        return cls(a, b)

    def print_area(self) -> None:
        print(f"Pole prostokata: {self.area}")


if __name__ == "__main__":
    r = Rectangle.load()
    if r is not None:
        r.calculate_area()
        r.print_area()
