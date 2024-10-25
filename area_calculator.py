def calculate_square_area(side):
    return side ** 2


def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    import math
    return math.pi * (radius ** 2)


def main():
    print("Калькулятор площадей фигур")
    print("Выберите фигуру для расчета площади:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Круг")
    
    choice = input("Введите номер фигуры (1-3): ")

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
    
    else:
        print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 3.")


if __name__ == "__main__":
    main()
