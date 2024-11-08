class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
       
        if not all(isinstance(side, (int, float)) for side in (self.a, self.b, self.c)):
            return "Нужно вводить только числа!"
        
       
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        
        
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

if __name__ == "__main__":
    try:
        a = float(input("Введите длину первого отрезка: "))
        b = float(input("Введите длину второго отрезка: "))
        c = float(input("Введите длину третьего отрезка: "))
        
        triangle_checker = TriangleChecker(a, b, c)
        result = triangle_checker.is_triangle()
        print(result)
    except ValueError:
        print("Нужно вводить только числа!")
