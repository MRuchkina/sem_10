import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Получаем все уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем новые столбцы для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

print(data)