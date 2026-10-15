import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# NO. 1
data = np.array([[1,2,3,4],[5,66,7,8]])
print(data)

# NO. 2
nilai2 = np.array([[1,2,3],[4,5,6]])
nilaihasil = nilai2.reshape(3,2)
print(nilaihasil)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
hasil = np.append(arr1, arr2)
print(hasil)

# NO. 3
a = np.arange(24)
b = a.reshape(2, 4, 3)
print(b)

# NO. 4
print(np.arange(2, 6, 5))

# NO. 5
a = np.array([3, 6, 9])
print(a)

# NO. 6
urutan = np.linspace(0, 10, 4, dtype=int)
print("Urutan:", urutan)

# NO. 7
# Pembagian antar elemen matriks
A = np.array([[2, 4], [10, 12]])
B = np.array([[1, 2], [5, 6]])
C = A / B
print(C)

# NO. 8
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
hasil = np.append(arr1, arr2)
print(hasil)

# NO. 9
# Membuat array NumPy
arr1 = np.array([1, 2, 3, 4, 5])
# Menyisipkan beberapa nilai sekaligus pada indeks ke-2
arr1_baru = np.insert(arr1, 2, [9, 9, 9])
print("Arr1 asli:", arr1)
print("Arr1 baru:", arr1_baru)