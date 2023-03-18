# Zadanie1

print("=====Zadanie 1:=====\n")

text1 = "Python 2023"
print(id(text1))
text2 = "Python 2023"
print(id(text2))
text3 = "Python 2023"
print(id(text3))

print('\n')

# Zadanie1_a

print("=====Zadanie 1a:=====\n")


print(text1==text2)
print(text2==text3)

print('\n')

# Zadanie1_b

print("=====Zadanie 1b:=====\n")


print(type(text1), hex(id(text1)))
print(type(text2), hex(id(text2)))
print(type(text3), hex(id(text3)))

text3 = "Java 11"

print('\n')

print(text1==text2)
print(text2==text3)

print('\n')

print(type(text1), hex(id(text1)))
print(type(text2), hex(id(text2)))
print(type(text3), hex(id(text3)))

print('\n')

# Zadanie2

print("=====Zadanie 2:=====\n")


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
        return first_num*second_num
    elif operator == "/":
        return first_num/second_num
    else:
        return None

print(f"Wynik operacji ({first_num} {operator} {second_num}) = {calculate(operator, first_num, second_num)}\n")

# Zadanie3

print("=====Zadanie 3:=====\n")

# pytania i odpowiedzi w formacie listowym
questions = [
    {
        "pytanie": "Jak masz na imię oraz nazwisko?",
    },
    {
        "pytanie": "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
        "odpowiedzi": ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki"]
    },
    {
        "pytanie": "W jakich okolicznościach czytasz książki najczęściej?",
        "odpowiedzi": ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "w ogóle nie czytam"]
    },
    {
        "pytanie": "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
        "odpowiedzi": ["chęć poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "czytanie to moje hobby"]
    },
    {
        "pytanie": "Po książki w jakiej formie sięgasz najczęściej?",
        "odpowiedzi": ["papierowej (tradycyjnej)", "e-booki (książki elektroniczne) na komputerze", "e-booki na specjalnym czytniku (Kindle)"]
    },
    {
        "pytanie": "Ile książek czytasz średnio w ciągu roku?",
        "odpowiedzi": ["0", "2 lub 3", "powyżej 10"]
    },
    {
        "pytanie": "Jak często średnio czytasz ksiązki",
        "odpowiedzi": ["codziennie", "raz w tygodniu", "raz w miesiącu"]
    },
    {
        "pytanie": "Po jakie gatunki książek sięgasz najczęściej?",
        "odpowiedzi": ["kryminały/thrillery", "romanse", "inne"]
    }

]

# odpowiedzi
answers = []

# pobranie odpowiedzi na pytania
for i in range(len(questions)): # iteracja po pytaniach
    question = questions[i]
    print(question["pytanie"])
    if i == 0: # jeżeli jest to pierwsze pytanie, to jest ono otwarte i odpowiedź na nie musi być podana przez użytkownika
        answer = input("odpowiedź: ")
        print("\n")
    else: # pozostałe pytania są pytaniami zamkniętymi
        for j in range(len(question["odpowiedzi"])): # iteracja po każdej odpowiedzi dla danego pytania # len(question) długość listy
            print(f"{j+1}. {question['odpowiedzi'][j]}") # wyświetl numer odpowiedzi oraz jej treść
        answer = input("Wybierz odpowiedź (wpisz numer): ")
        print("\n")
        answer = question["odpowiedzi"][int(answer)-1] # -1 bo numeracja odpowiedzi zaczyna się od jeden a indeksowanie od zera
    answers.append(answer)

# wyświetlenie odpowiedzi
print("\nUdzielone odpowiedzi na zadane pytania:")
for i in range(len(questions)):
    print(f"pytanie: {questions[i]['pytanie']}")
    print(f"odpowiedź: {answers[i]}\n")

