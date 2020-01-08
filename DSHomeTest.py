import numpy as np
from sklearn import preprocessing

Input_data = np.array([
    [2.1, -1.9, 5.5],
    [-1.5, 2.4, 3.5],
    [0.5, -7.9, 5.6],
    [5.9, 2.3, -5.8]
])

input_labels = ['red', 'black', 'red', 'green',
                'black', 'yellow', 'white']

encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
# print(list(encoded_values))

encoded_values1 = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values1)
print(list(decoded_list))
