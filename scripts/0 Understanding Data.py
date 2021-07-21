from pathlib import Path
import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt


# it is the path from where you initiate script
path = Path('C:/Users/dell/3D Objects/Coronavirus X-ray project - Major/Data')

covid_without_PNEUMONIA_train_path = path / 'train' / 'covid_without_PNEUMONIA'
covid_with_PNEUMONIA_train_path = path / 'train' / 'covid_with_PNEUMONIA'

covid_without_PNEUMONIA_test_path = path / 'test' / 'covid_without_PNEUMONIA'
covid_with_PNEUMONIA_test_path = path / 'test' / 'covid_with_PNEUMONIA'



covid_without_PNEUMONIA_path = [covid_without_PNEUMONIA_train_path, covid_without_PNEUMONIA_test_path]
covid_with_PNEUMONIA_path = [covid_with_PNEUMONIA_train_path, covid_with_PNEUMONIA_test_path]


np.random.seed(42)
random.seed(42)

label2category = {'covid_without_PNEUMONIA': 0, 'covid_with_PNEUMONIA': 1}
category2label = {0: 'covid_without_PNEUMONIA', 1: 'covid_with_PNEUMONIA'}
data = []

for path in covid_without_PNEUMONIA_path:
    for img in path.glob('*.jpeg'):
        data.append({'img_path': str(img), 'label': 'covid_without_PNEUMONIA'})
    
for path in covid_with_PNEUMONIA_path:
    for img in path.glob('*.jpeg'):
        data.append({'img_path': str(img), 'label': 'covid_with_PNEUMONIA'})
        
np.random.shuffle(data)


def counter_label(data=None, key=None, index=None):
    label = []
    for value in data:
        label.append(value[key])
    return Counter(label)


img_l_counter = counter_label(data, 'label')
keys = list(img_l_counter.keys())
values = list(img_l_counter.values())

print(len(data), path)


fig = plt.figure(figsize = (10, 5))
plt.bar(keys, values, color =['red', 'yellow'], align='center', width = 0.7, edgecolor='green')

plt.xlabel('Class')
plt.ylabel('Number of Images')
plt.title('Pneumonia vs No Pneumonia')
plt.show()
