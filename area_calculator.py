def calculate_square_area(side):
    return side ** 2


def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    import math
    return math.pi * (radius ** 2)


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_parallelogram_area(base, height):
    return base * height


def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


def main():
    print("Калькулятор площадей фигур")
    print("Выберите фигуру для расчета площади:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Круг")
    print("4. Треугольник")
    print("5. Параллелограмм")
    print("6. Трапеция")

    choice = input("Введите номер фигуры (1-6): ")

    try:
        if choice == '1':
            side = float(input("Введите длину стороны квадрата: "))
            area = calculate_square_area(side)
            print(f"Площадь квадрата: {area:.2f}")

        elif choice == '2':
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            area = calculate_rectangle_area(length, width)
            print(f"Площадь прямоугольника: {area:.2f}")

        elif choice == '3':
            radius = float(input("Введите радиус круга: "))
            area = calculate_circle_area(radius)
            print(f"Площадь круга: {area:.2f}")

        elif choice == '4':
            base = float(input("Введите длину основания треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            area = calculate_triangle_area(base, height)
            print(f"Площадь треугольника: {area:.2f}")

        elif choice == '5':
            base = float(input("Введите длину основания параллелограмма: "))
            height = float(input("Введите высоту параллелограмма: "))
            area = calculate_parallelogram_area(base, height)
            print(f"Площадь параллелограмма: {area:.2f}")

        elif choice == '6':
            base1 = float(input("Введите длину первого основания трапеции: "))
            base2 = float(input("Введите длину второго основания трапеции: "))
            height = float(input("Введите высоту трапеции: "))
            area = calculate_trapezoid_area(base1, base2, height)
            print(f"Площадь трапеции: {area:.2f}")

        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 6.")

    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числовые значения.")


if __name__ == "__main__":
    main()
