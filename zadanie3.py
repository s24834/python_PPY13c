import random
from getpass import getpass

# ZADANIA

# Zadanie_1

print("=====Zadanie1=====")

numbers = input("Podaj liczby po przecinku:")

list_of_numbers = numbers.split(",")

list_of_numbers = [int(number) for number in list_of_numbers]

print(list_of_numbers)


def minmax(x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum:
                maximum = i
    return minimum, maximum


print(minmax(list_of_numbers))


# Zadanie_2

print("\n=====Zadanie2=====")

cities = "Warszawa,Kraków,Łódź,Poznań,Gdańsk,Tarnów,Bydgoszcz,Lublin,Płock,Katowice"
cities_list = cities.split(",")
print(f"lista miast: {cities_list}")

city = random.sample(cities_list, len(cities_list))
print(city)


# Zadanie_3

print("\n=====Zadanie3=====")


def play_game(rounds, mode):

    # w zależności od trybu gry
    if mode == 1:
        p1_name = input("\nPodaj nazwę gracza: ")
        p2_name = "Komputer"
    elif mode == 2:
        p1_name = input("\nPodaj nazwę gracza 1: ")
        p2_name = input("Podaj nazwę gracza 2: ")

    scores = []

    # rundy
    for i in range(1, rounds + 1):
        print(f"\nRunda {i}.")

        round_score = {p1_name: 0, p2_name: 0}

        # podawanie swojego wyboru
        if mode == 1:
            p1_choice = int(input(f"{p1_name}, podaj swój wybór (1-papier, 2-nożyce, 3-kamień): "))
            p2_choice = random.randint(1, 3)
            print(f"{p2_name}, podaje swój wybór (1-papier, 2-nożyce, 3-kamień): {p2_choice}")
        elif mode == 2:
            p1_choice = int(getpass(f"{p1_name}, podaj swój wybór (1-papier, 2-nożyce, 3-kamień): "))
            p2_choice = int(getpass(f"{p2_name}, podaj swój wybór (1-papier, 2-nożyce, 3-kamień): "))

        # punktacja poszczególnych rund
        if p1_choice == p2_choice:
            print("Remis!")
            round_score[p1_name] += 1
            round_score[p2_name] += 1

        elif (p1_choice == 1 and p2_choice == 2) or (p1_choice == 2 and p2_choice == 3) or (p1_choice == 3 and p2_choice == 1):
            print(f"{p2_name} wygrywa rundę!")
            round_score[p2_name] += 1

        else:
            print(f"{p1_name} wygrywa rundę!")
            round_score[p1_name] += 1

        scores.append(round_score)

    print("\nWyniki poszczególnych rund:")

    for i, round_score in enumerate(scores):
        print(f"\n~Runda {i+1}.~")
        for player, score in round_score.items():
            print(f"{player}: {score}")

    # wynik ostateczny całej gry
    final_scores = {p1_name: 0, p2_name: 0}

    for round_score in scores:
        final_scores[p1_name] += round_score[p1_name]
        final_scores[p2_name] += round_score[p2_name]

    if final_scores[p1_name] > final_scores[p2_name]:
        print(f"\nWynik rozgrywki: {final_scores[p1_name]}:{final_scores[p2_name]} dla {p1_name}")
        print(f"\nGracz {p1_name} wygrywa grę uzyskując niesamowity wynik: {final_scores[p1_name]} punktów!")
    elif final_scores[p2_name] > final_scores[p1_name]:
        print(f"\nWynik rozgrywki: {final_scores[p2_name]}:{final_scores[p1_name]} dla {p2_name}")
        print(f"\nGracz {p2_name} wygrywa grę uzyskując niesamowity wynik: {final_scores[p2_name]} punktów!")
    else:
        print(f"\nWynik rozgrywki: {final_scores[p1_name]}:{final_scores[p2_name]}")
        print(f"\nNiesamowity Remis! Oboje graczy uzyskało ten sam wynik: {final_scores[p2_name]} punktów!")


def main():
    print("Witaj w grze Papier-Kamień-Nożyce!")
    rounds = int(input("\nPodaj liczbę rund: "))

    while True:
        print("\nWybierz tryb gry:")
        print("1. Gra z komputerem")
        print("2. Gra w hot seats")
        mode = int(input("Wybierz tryb gry (1 lub 2): "))
        if mode in [1, 2]:
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

    play_game(rounds, mode)


if __name__ == '__main__':
    main()
