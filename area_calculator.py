"""
Калькулятор площадей фигур

Это консольное приложение, которое позволяет пользователю
вычислять площади различных геометрических фигур, таких как
квадраты, прямоугольники, круги, треугольники, параллелограммы,
трапеции и многоугольники. Программа также предоставляет
возможность сравнения площадей двух фигур.
"""


def calculate_square_area(side):
    """
    Вычисляет площадь квадрата.

    :param side: Длина стороны квадрата.
    :return: Площадь квадрата (float).
    """
    return side**2


def calculate_rectangle_area(length, width):
    """
    Вычисляет площадь прямоугольника.

    :param length: Длина прямоугольника.
    :param width: Ширина прямоугольника.
    :return: Площадь прямоугольника (float).
    """
    return length * width


def calculate_circle_area(radius):
    """
    Вычисляет площадь круга.

    :param radius: Радиус круга.
    :return: Площадь круга (float).
    """
    import math
    return math.pi * (radius**2)


def calculate_triangle_area(base, height):
    """
    Вычисляет площадь треугольника.

    :param base: Длина основания треугольника.
    :param height: Высота треугольника.
    :return: Площадь треугольника (float).
    """
    return 0.5 * base * height


def calculate_parallelogram_area(base, height):
    """
    Вычисляет площадь параллелограмма.

    :param base: Длина основания параллелограмма.
    :param height: Высота параллелограмма.
    :return: Площадь параллелограмма (float).
    """
    return base * height


def calculate_trapezoid_area(base1, base2, height):
    """
    Вычисляет площадь трапеции.

    :param base1: Длина первого основания трапеции.
    :param base2: Длина второго основания трапеции.
    :param height: Высота трапеции.
    :return: Площадь трапеции (float).
    """
    return 0.5 * (base1 + base2) * height


def calculate_polygon_area(coords):
    """
    Вычисляет площадь многоугольника по координатам его вершин.

    :param coords: Список координат вершин многоугольника [(x1, y1), (x2, y2), ...].
    :return: Площадь многоугольника (float).
    """
    n = len(coords)
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2


def compare_areas(area1, area2):
    """
    Сравнивает площади двух фигур.

    :param area1: Площадь первой фигуры (float).
    :param area2: Площадь второй фигуры (float).
    :return: Строка с результатом сравнения.
    """
    if area1 > area2:
        return "Первая фигура больше второй."
    elif area1 < area2:
        return "Вторая фигура больше первой."
    else:
        return "Фигуры равны по площади."


def main():
    """
    Главная функция программы.

    Запрашивает у пользователя выбор действия и фигуры,
    затем выполняет соответствующие расчеты.
    """
    print("Калькулятор площадей фигур")
    print("Выберите действие:")
    print("1. Вычислить площадь фигуры")
    print("2. Сравнить площади двух фигур")

    action = input("Введите номер действия (1-2): ")

    if action == '1':
        print("Выберите фигуру для расчета площади:")
        print("1. Квадрат")
        print("2. Прямоугольник")
        print("3. Круг")
        print("4. Треугольник")
        print("5. Параллелограмм")
        print("6. Трапеция")
        print("7. Многоугольник (по координатам)")

        choice = input("Введите номер фигуры (1-7): ")

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

            elif choice == '7':
                coords = []
                num_vertices = int(input("Введите количество вершин многоугольника: "))
                for i in range(num_vertices):
                    x = float(input(f"Введите x координату вершины {i + 1}: "))
                    y = float(input(f"Введите y координату вершины {i + 1}: "))
                    coords.append((x, y))
                area = calculate_polygon_area(coords)
                print(f"Площадь многоугольника: {area:.2f}")

            else:
                print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 7.")

        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовые значения.")
    elif action == '2':
        print("Выберите фигуры для сравнения площадей:")
        print("1. Квадрат")
        print("2. Прямоугольник")
        print("3. Круг")
        print("4. Треугольник")
        print("5. Параллелограмм")
        print("6. Трапеция")

        choice1 = input("Введите номер первой фигуры (1-6): ")
        choice2 = input("Введите номер второй фигуры (1-6): ")

        try:
            if choice1 == '1':
                side1 = float(input("Введите длину стороны первого квадрата: "))
                area1 = calculate_square_area(side1)
            elif choice1 == '2':
                length1 = float(input("Введите длину первого прямоугольника: "))
                width1 = float(input("Введите ширину первого прямоугольника: "))
                area1 = calculate_rectangle_area(length1, width1)
            elif choice1 == '3':
                radius1 = float(input("Введите радиус первого круга: "))
                area1 = calculate_circle_area(radius1)
            elif choice1 == '4':
                base1 = float(input("Введите длину основания первого треугольника: "))
                height1 = float(input("Введите высоту первого треугольника: "))
                area1 = calculate_triangle_area(base1, height1)
            elif choice1 == '5':
                base1 = float(input("Введите длину основания первого параллелограмма: "))
                height1 = float(input("Введите высоту первого параллелограмма: "))
                area1 = calculate_parallelogram_area(base1, height1)
            elif choice1 == '6':
                base1 = float(input("Введите длину первого основания трапеции: "))
                base2_1 = float(input("Введите длину второго основания трапеции: "))
                height1 = float(input("Введите высоту трапеции: "))
                area1 = calculate_trapezoid_area(base1, base2_1, height1)

            else:
                print("Некорректный ввод для первой фигуры.")
                return

            if choice2 == '1':
                side2 = float(input("Введите длину стороны второго квадрата: "))
                area2 = calculate_square_area(side2)
            elif choice2 == '2':
                length2 = float(input("Введите длину второго прямоугольника: "))
                width2 = float(input("Введите ширину второго прямоугольника: "))
                area2 = calculate_rectangle_area(length2, width2)
            elif choice2 == '3':
                radius2 = float(input("Введите радиус второго круга: "))
                area2 = calculate_circle_area(radius2)
            elif choice2 == '4':
                base2 = float(input("Введите длину основания второго треугольника: "))
                height2 = float(input("Введите высоту второго треугольника: "))
                area2 = calculate_triangle_area(base2, height2)
            elif choice2 == '5':
                base2 = float(input("Введите длину основания второго параллелограмма: "))
                height2 = float(input("Введите высоту второго параллелограмма: "))
                area2 = calculate_parallelogram_area(base2, height2)
            elif choice2 == '6':
                base2_2 = float(input("Введите длину первого основания второй трапеции: "))
                base2_2_2 = float(input("Введите длину второго основания второй трапеции: "))
                height2 = float(input("Введите высоту второй трапеции: "))
                area2 = calculate_trapezoid_area(base2_2, base2_2_2, height2)

            else:
                print("Некорректный ввод для второй фигуры.")
                return

            result = compare_areas(area1, area2)
            print(result)

        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовые значения.")

    else:
        print("Некорректный ввод. Пожалуйста, выберите номер действия от 1 до 2.")


if __name__ == "__main__":
    main()
