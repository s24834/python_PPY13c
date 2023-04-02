import math

# ZADANIA
print("=====ZADANIA=====")

# Zadanie_1

print("\nZadanie_1")


def panel_calc(dl_podlogi, sz_podlogi, dl_panela, sz_panela, ilosc_paneli_opakowanie):
    # powierzchnia = dl_podlogi * sz_podlogi * 1.1

    il_paneli_poziom = sz_podlogi * 1.1 / sz_panela

    il_paneli_pion = dl_podlogi * 1.1 / dl_panela

    il_paneli_total = il_paneli_poziom * il_paneli_pion  # * powierzchnia

    # il_paneli_opakowanie = ilosc_paneli_opakowanie

    il_opakowan = math.ceil(il_paneli_total / ilosc_paneli_opakowanie)

    # il_paneli_pion = il_paneli_total / ilosc_paneli_opakowanie

    return il_opakowan


print("Potrzeba: " + str(panel_calc(4, 4, 0.20, 1, 10)) + " opakowań paneli w danym pomieszczeniu")

# Zadanie_2

print("\nZadanie_2")


def is_prime(number):
    a = 2
    while a <= math.sqrt(number):
        if number % a < 1:
            print(f"Liczba {number} nie jest liczbą pierwszą")
            return False
        a = a + 1
    print(f"Liczba {number} jest liczbą pierwszą")
    return number > 1


is_prime(47)  # wywołanie funkcji

# Zadanie_3

print("\nZadanie_3")

"""
    funkcja przyjmuje następujące argumenty:
    message - tekst do zaszyfrowania,
    key - liczbę, o ile należy przesunąć litery w alfabecie
    [alphabet] - opcjonalnie przyjmuje dowolny alfabet (domyślnie używany alfabet angielski)

    używając modulo (%) funkcja rozwiązuje problem klucza przesuwającego litery poza zakres tablicy z alfabetem
    oraz problem podania klucza o dowolnej wielkości

    funkcja zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string
"""


# funkcja szyfrująca wiadomość szyfrem cezara
def caesar_cipher(message, key, alphabet=None):
    if alphabet is None:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()  # zamiana wszystkich liter na małe litery
    ciphered_message = ''
    for letter in message:
        # funkcja szyfruje tylko litery
        if letter in alphabet:  # jeśli dany znak jest literą z wiadomości
            index = alphabet.index(letter)  # znajdywanie indeksu litery w alfabecie
            # obliczanie indeksu litery zaszyfrowanej (dodawanie klucza oraz operacja modulo)
            ciphered_index = (index + key) % len(alphabet)
            ciphered_letter = alphabet[ciphered_index]
            ciphered_message += ciphered_letter
        # – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian
        else:
            ciphered_message += letter
    return ciphered_message


data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"

enc_1 = caesar_cipher(data, 5)
enc_2 = caesar_cipher(data, 3, ["a", "B"])

print(f"coded message 1.: {enc_1}")
print("===")
print(f"coded message 2.: {enc_2}")