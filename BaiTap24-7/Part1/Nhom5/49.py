a = float(input(" Nhap so thu nhat : "))
b = float(input(" Nhap so thu hai : "))
phep_toan = input(" Nhap phep toan (+ , -, * , /) : ")

if phep_toan == "+":
    ket_qua = a + b
elif phep_toan == "-":
    ket_qua = a - b
elif phep_toan == "*":
    ket_qua = a * b
elif phep_toan == "/":
    if b != 0:
        ket_qua = a / b
    else:
        print(" Loi : Khong the chia cho 0 ")
        ket_qua = None
else:
    print(" Phep toan khong hop le ")
    ket_qua = None

if ket_qua is not None:
    print(f"{ket_qua}")
