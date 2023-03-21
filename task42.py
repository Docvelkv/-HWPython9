# Узнать какая максимальная households в зоне минимального значения population.
import pandas as pnd

main_csv = pnd.read_csv("california_housing_test.csv")
ppl = main_csv['population']
hhs = main_csv['households']
print(hhs[ppl == ppl.min()].max())  # во всей таблице такая строка одна
print(hhs[ppl == ppl.min()])  # искать максимальное значение не обязательно
