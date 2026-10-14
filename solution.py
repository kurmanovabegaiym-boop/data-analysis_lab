import numpy as np

# Закидываем исходные данные задачи
order_id = np.array([1001, 1002, 1003, 1004, 1005, 1006])
quantity = np.array([2, 3, 0, 5, -1, 4])
unit_price = np.array([1500, 2000, 1200, 3000, 2500, np.nan])
discount = np.array([0.10, 0.05, 0.00, 0.15, 0.10, 0.20])


# --- Задание 1. Проверяем структуру ---
print("=== Задание 1: Размеры и типы ===")
for name, arr in [('order_id', order_id), ('quantity', quantity), ('unit_price', unit_price), ('discount', discount)]:
    print(f"Массив {name}: размер={arr.size}, форма={arr.shape}, тип={arr.dtype}")

print("\nВывод: Все массивы одномерные и одинаковой длины, поэтому пока по индексам всё сходится.\n")


# --- Задание 2. Контроль качества (маски) ---
print("=== Задание 2: Ищем косяки в данных ===")
bad_qty = (quantity <= 0)
missing_price = np.isnan(unit_price)
bad_disc = (discount < 0) | (discount > 1)
all_bad = bad_qty | missing_price | bad_disc

print("Нулевое или минусовое количество:", bad_qty)
print("Где нет цен (NaN):", missing_price)
print("Скидки не от 0 до 1:", bad_disc)
print("Общая маска проблемных строк:", all_bad)
print()


# --- Задание 3. Собираем рабочий нормальный набор ---
print("=== Задание 3: Очистка данных ===")
good_qty = quantity > 0
good_price = np.isfinite(unit_price) & (unit_price >= 0)
good_disc = (discount >= 0) & (discount <= 1)

ok_mask = good_qty & good_price & good_disc

clean_id = order_id[ok_mask]
clean_qty = quantity[ok_mask]
clean_price = unit_price[ok_mask]
clean_disc = discount[ok_mask]

print("Нормальные ID заказов:", clean_id)
print("Чистые цены:", clean_price)
print("\nПочему нельзя резать каждый массив отдельно? Потому что они разъедутся по длине и индексам, и цена от одного заказа случайно привяжется к ID другого.\n")


# --- Задание 4. Делаем матрицу ---
print("=== Задание 4: Матрица параметров ===")
# Соединяем всё в одну табличку
my_matrix = np.column_stack((clean_qty, clean_price, clean_disc))
print("Форма матрицы:", my_matrix.shape)
print(my_matrix)
print("\nСобрали так, чтобы строки были заказами, а столбцы — параметрами. Это классика для математических расчетов в numpy.\n")


# --- Задание 5. Меняем форму (reshape) ---
print("=== Задание 5: Изменяем форму массива (reshape) ===")
sales_24 = np.arange(1, 25)

m_4x6 = sales_24.reshape(4, 6)
m_6x4 = sales_24.reshape(6, 4)

print("Матрица 4 на 6 (недели х категории):\n", m_4x6)
print("\nМатрица 6 на 4 (категории х недели):\n", m_6x4)
print("\nЭлементов столько же (24), но смысл поменялся: теперь строки значат совсем другое.\n")


# --- Задание 6. Проверяем сторонние файлы ---
print("=== Задание 6: Если файлы не сходятся ===")
fake_price = np.array([1500, 2000, 1200, 3000, 2500]) # типа потеряли одну цену
match_check = (order_id.size == fake_price.size)
print("Длины совпадают?", match_check)
print("\nДаже если бы длинна совпала (например, одна строка продублировалась, а другая пропала), данные всё равно могли перепутаться. Нужна проверка ID.\n")


# --- Задание 7. Проверка для аналитики ---
print("=== Задание 7: Проверка матрицы регионов ===")
regions_sales = np.array([
    [12000, 15000, 13500, 14200, 16000, 15500],
    [9800,  10200, 11000, 10500, 11200, 11800],
    [20000, 21500, 22000, 21000, 22500, 23000],
    [8500,  9100,  8900,  9400,  9600,  9900]
])
print("Нет пропусков/бесконечностей?", np.all(np.isfinite(regions_sales)))
print("Нет отрицательных продаж?", np.all(regions_sales >= 0))
print()


# --- Задание 8. Выводы ---
print("=== Задание 8: Краткий отчёт по качеству ===")
print("""
Короче говоря по данным:
- Главные проблемы: нули/минусы в штуках и пропущенные цены (NaN). Без чистки анализировать нельзя, всё сломается.
- Мелкие вопросы: скидки вроде в норме, но надо глянуть, нет ли диких цифр.
""")


# --- Доп. задание ---
print("=== Доп. задание: Функция проверки массива ===")
def check_numeric_array(arr):
    return {
        "shape": arr.shape,
        "missing": int(np.isnan(arr).sum()) if np.issubdtype(arr.dtype, np.inexact) else 0,
        "negatives": int((arr < 0).sum()) if np.issubdtype(arr.dtype, np.number) else 0
    }

print("Результат проверки цен:", check_numeric_array(unit_price))