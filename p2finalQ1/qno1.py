print("Question no 01")
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

dec_val = int(input("Enter the number you want to convert in binary:"))
DecimalToBinary(dec_val)