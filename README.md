# README

## Описание программы

Данная консольная программа на Python предназначена для вычисления площади различных геометрических фигур и сравнения площадей двух фигур.

## Функционал

Программа поддерживает следующие фигуры:

1. **Квадрат**: Площадь вычисляется по формуле \( S = a^2 \), где \( a \) — длина стороны.
2. **Прямоугольник**: Площадь вычисляется по формуле \( S = l \times w \), где \( l \) — длина, \( w \) — ширина.
3. **Круг**: Площадь вычисляется по формуле \( S = \pi r^2 \), где \( r \) — радиус.
4. **Треугольник**: Площадь вычисляется по формуле \( S = \frac{1}{2} \times b \times h \), где \( b \) — основание, \( h \) — высота.
5. **Параллелограмм**: Площадь вычисляется по формуле \( S = b \times h \), где \( b \) — основание, \( h \) — высота.
6. **Трапеция**: Площадь вычисляется по формуле \( S = \frac{1}{2} \times (b_1 + b_2) \times h \), где \( b_1 \) и \( b_2 \) — основания, \( h \) — высота.
7. **Многоугольник**: Площадь вычисляется по формуле Герона с вводимыми координатами вершин многоугольника.

## Возможности

1. **Вычисление площади фигуры**: Пользователь может выбрать фигуру и ввести необходимые параметры для вычисления её площади.
2. **Сравнение площадей**: Пользователь может выбрать две фигуры и сравнить их площади, чтобы определить, какая из них больше.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.x. Если Python не установлен, вы можете скачать его с [официального сайта](https://www.python.org/downloads/).
2. Скачайте файл с программой (например, `main.py`) с помощью браузера или другого способа.
3. Перейдите в папку, где находится скачанный файл, с помощью командной строки.

## Запуск программы

Для запуска программы выполните следующую команду в терминале:

```bash
python main.py
```

## Примеры использования

**Вычисление площади круга:**

```
Калькулятор площадей фигур
Выберите действие:
1. Вычислить площадь фигуры
2. Сравнить площади двух фигур
Введите номер действия (1-2): 1
Выберите фигуру для расчета площади:
1. Квадрат
2. Прямоугольник
3. Круг
4. Треугольник
5. Параллелограмм
6. Трапеция
7. Многоугольник (по координатам)
Введите номер фигуры (1-7): 3
Введите радиус круга: 12
Площадь круга: 452.39
```

**Сравнение площадей квадрата и прямоугольника:**

```
Калькулятор площадей фигур
Выберите действие:
1. Вычислить площадь фигуры
2. Сравнить площади двух фигур
Введите номер действия (1-2): 2
Выберите фигуры для сравнения площадей:
1. Квадрат
2. Прямоугольник
3. Круг
4. Треугольник
5. Параллелограмм
6. Трапеция
Введите номер первой фигуры (1-6): 1
Введите номер второй фигуры (1-6): 2
Введите длину стороны первого квадрата: 5
Введите длину второго прямоугольника: 2
Введите ширину второго прямоугольника: 15
Вторая фигура больше первой.
```

## Документация

Подробная документация представлена файлами с расширениями *.html* и *.xml*  
**HTML:** docs/html/index.html  
**.xml:** docs/docbook/index.xml
