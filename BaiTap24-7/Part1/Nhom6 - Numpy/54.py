import numpy as np

number = 1000

ket_qua = np.random.choice([0, 1], size=number)

sap = np.sum(ket_qua == 0)
ngua = np.sum(ket_qua == 1)

print(f"Sap: {sap}, Ngua: {ngua}")
