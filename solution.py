import numpy as np


order_id = np.array([1001, 1002, 1003, 1004, 1005, 1006])
quantity = np.array([2, 3, 0, 5, -1, 4])
unit_price = np.array([1500, 2000, 1200, 3000, 2500, np.nan])
discount = np.array([0.10, 0.05, 0.00, 0.15, 0.10, 0.20])


print("--- Задание 1: Структура массивов ---")
for name, arr in [('order_id', order_id), ('quantity', quantity), ('unit_price', unit_price), ('discount', discount)]:
    print(f"Массив {name}:")
    print(f"  Размер (size): {arr.size}")
    print(f"  Форма (shape): {arr.shape}")
    print(f"  Измерения (ndim): {arr.ndim}")
    print(f"  Тип (dtype): {arr.dtype}")

print("\n--- Задание 2: Контроль качества ---")
invalid_quantity = (quantity <= 0)
missing_price = np.isnan(unit_price)
invalid_discount = (discount < 0) | (discount > 1)

print("Заказы с нулевым или отрицательным количеством:", invalid_quantity)
print("Цены с пропущенными значениями:", missing_price)
print("Недопустимые скидки:", invalid_discount)


bad_orders = invalid_quantity | missing_price | invalid_discount
print("Заказы, не прошедшие первичную проверку:", bad_orders)