import numpy as np
import pandas as pd
import random
file = 'california_housing_train.csv'
####################
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
####################
unique_values = list(set(data['whoAmI'])) #Создаем список уникальных значений столбца whoAmI

num_values = len(unique_values) #Определяем количество уникальных значений в списке

value_dict = dict(zip(unique_values, range(num_values))) #Создаем словарь, где каждому уникальному
                                                         # значению столбца whoAmI будет соответствовать свой номер

one_hot = np.zeros((len(data), num_values), int) #Создаем пустой массив нужного размера и заполняем его нулями

for i in range(len(data)):
    one_hot[i, value_dict[data.iloc[i]['whoAmI']]] = 1 #Проходим по каждой строке DataFrame
                                                       # и для каждой строки заполняем массив единицами
                                                       # в соответствующих местах

one_hot_df = pd.DataFrame(one_hot, columns=unique_values) #Создаем новый DataFrame на основе полученного массива,
                                                          # где столбцы называются уникальными значениями столбца whoAmI

data.drop('whoAmI', axis=1, inplace=True) #Удаляем старый столбец whoAmI из исходного DataFrame.
data = pd.concat([data, one_hot_df], axis=1) # Объединяем два DataFrame в один по столбцам
print(data.head())

#Вывод

#   human  robot
#0    0      1
#1    0      1
#2    1      0
#3    0      1
#4    0      1
