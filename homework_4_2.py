'''Задача 2. Возврат бракованных батончиков'''

result_bad = []

while True:
    mass = int(input())
    if mass == 0:
        break
    if not 40 <= mass <= 50:
        result_bad.append(mass)

print(result_bad[::-1])