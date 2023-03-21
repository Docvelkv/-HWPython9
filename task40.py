# Работать с файлом california_housing_train.csv. Определить среднюю стоимость
# дома, где кол-во людей от 0 до 500 (population).
import pandas as pnd

main_csv = pnd.read_csv("california_housing_test.csv")
ppl = main_csv['population']
mhv = main_csv['median_house_value']
print(mhv[(ppl > 0) & (ppl < 500)].mean())  # средняя арифметическая стоимость
print(mhv[(ppl > 0) & (ppl < 500)].median())  # срединное значение
