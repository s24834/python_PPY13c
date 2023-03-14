# # Zadanie1
#
# text1 = "Python 2023"
# print(id(text1))
# text2 = "Python 2023"
# print(id(text2))
# text3 = "Python 2023"
# print(id(text3))
#
# print('\n')
#
# # a
#
# print(text1==text2)
# print(text2==text3)
#
# # b
#
# print(type(text1), hex(id(text1)))
# print(type(text2), hex(id(text2)))
# print(type(text3), hex(id(text3)))
#
# print('\n')
#
# text3 = "Java 11"
#
# print(text1==text2)
# print(text2==text3)
#
# print(type(text1), hex(id(text1)))
# print(type(text2), hex(id(text2)))
# print(type(text3), hex(id(text3)))

# Zadanie2

print("=====Kalkulator=====")

first_num = int(input("Podaj pierwszą liczbę: "))
second_num = int(input("Podaj drugą liczbę: "))
operator = input("Użyj jednego z podanych operatorów ( +, -, *, / ) ")

def calculate(operator, first_num, second_num):
    if operator == "+":
        return first_num+second_num
    elif operator == "-":
        return first_num-second_num
    elif operator == "*":
        return first_num+second_num
    elif operator == "/":
        return first_num/second_num
    else:
        return None

print(calculate(operator, first_num, second_num))
