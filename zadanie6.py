# Używając dodatkowo klasy:
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


# Napisz klasę MyLinkedList – która będzie posortowana,wiązana oraz jednostronna.
class MyLinkedList:
    # Klasa MyLinkedList zawiera pola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # z metodami:
    # __str__ - reprezentacja napisowa listy – wszystkie elementy listy
    def __str__(self):
        if self.size == 0:
            return "Empty LinkedList"
        else:
            current = self.head
            result = []  # przechowywanie wyniku (napisowej reprezentacji listy)
            while current is not None:
                result.append(str(current.data))  # dodawanie do listy wynikowej elementów listy za pomocą metody append()
                current = current.nextE
            return ", ".join(result)  # zwracanie napisowej reprezentacji listy

    # get(self, e) – zwraca element
    def get(self, e):
        current = self.head  # początek
        while current is not None:
            if current.data == e:  # porównywanie kolejnego elementu listy z wartością szukaną e
                return current  # zwrócenie obiektu, który reprezentuje dany element listy
            current = current.nextE  # zmiana na kolejny element z listy
        return None  # jeżeli nie znaleziono elementu e

    # delete(self,e) – usuwa wskazany element
    def delete(self, e):
        current = self.head  # ustawienie wskaźnika na początku listy
        previous = None
        while current is not None:  # przeglądanie wartości listy, dopóki ta nie będzie pusta
            if current.data == e:  # czy wartość elementu jest równa wartości elementu poszukiwanemu
                # znaleźliśmy usuwany element
                if previous is not None:  # nie jest to element początkowy listy
                    previous.nextE = current.nextE  # pominięcie elementu, który chcemy usunąć
                    if current.nextE is None:  # jeśli usuwamy element końcowy
                        self.tail = previous
                else:
                    self.head = current.nextE
                    if self.head is None:
                        self.tail = None
                self.size -= 1
                return True  # usunięto
            previous = current
            current = current.nextE  # zmiana wartości na kolejną
        return False  # nie ma elementu do usunięcia

    # append (self, e, func=None) – dodaje elementy do listy w sposób posortowany
    # func – jaki będzie warunek sortownia – określi funkcja, jeżeli None – zwykłe porównanie 2 obiektów za pomocą >=
    def append(self, e, func=None):
        element = Element(e)
        if self.head is None:  # jeśli lista jest pusta
            self.head = element  # ten sam początek (bo jeden element)
            self.tail = element  # ten sam koniec (bo jeden element)
            self.size = 1  # jeden element w liście
            return

        # jeśli lista nie jest pusta
        # domyślne sortowanie
        if func is None:
            func = lambda a, b: a >= b  # domyślne umieszczanie elementów w kolejności malejącej
        if func(self.tail.data, e):
            # element dodawany jako ostatni element listy
            self.tail.nextE = element
            self.tail = element
            self.size += 1  # zwiększenie rozmiaru listy o jeden
            return

        current = self.head
        previous = None
        while current is not None:
            if func(e, current.data):  # jeżeli wartość elementu e jest większa od aktualnego elementu
                if previous is not None:
                    previous.nextE = element  # przechodzimy do kolejnego elementu
                else:
                    self.head = element
                element.nextE = current
                self.size += 1
                return
            previous = current
            current = current.nextE


# TEST

# tworzenie listy
my_linked_list = MyLinkedList()

# dodawanie elementów do naszej listy
my_linked_list.append(5)
my_linked_list.append(10)
my_linked_list.append(2)
my_linked_list.append(8)
my_linked_list.append(1)
my_linked_list.append(15)
my_linked_list.append(3)

# wyświetlanie zawartości naszej listy
print(my_linked_list)

# usuwanie elementów z listy
my_linked_list.delete(5)
my_linked_list.delete(15)

# wyświetlanie zawartości listy po usunięciu elementów
print(my_linked_list)

# pobieranie elementów z listy
print(my_linked_list.get(8))
print(my_linked_list.get(15))  # None


import smtplib
from email.mime.text import MIMEText
from typing import List
from dataclasses import dataclass


@dataclass
class Student:
    email: str
    first_name: str
    last_name: str
    project_points: int
    list_points: list[int]
    homework_points: list[int]
    final_grade: float
    status: str

    # funkcja do automatycznego wystawienia oceny
    def grade_student(self):
        if self.status not in ['GRADED', 'MAILED']:
            if self.project_points == -1:
                return
            points = self.project_points
            if min(self.list_points) == -1:
                return
            list_p = self.list_points
            if min(self.homework_points) == -1:
                return
            points_sum: int = sum(self.homework_points)

            if points_sum >= 600:
                list_p[list_p.index(min(list_p))] = 20
            if points_sum >= 700:
                list_p[list_p.index(min(list_p))] = 20
            if points_sum >= 800:
                list_p[list_p.index(min(list_p))] = 20

            points += sum(list_p)

            print(points)

            if points >= 91:
                grade = 5.0
            elif points >= 81:
                grade = 4.5
            elif points >= 71:
                grade = 4.0
            elif points >= 61:
                grade = 3.5
            elif points >= 51:
                grade = 3.0
            else:
                grade = 2.0
            self.status = 'GRADED'
            self.final_grade = grade
            print(f'Ocena {self.final_grade} wystawiona dla studenta o adresie email {self.email}.')

    # wysyłanie maila
    def send_email(self, subject, body, sender: str, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = self.email

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)

        smtp_server.sendmail(sender, self.email, msg.as_string())

        smtp_server.quit()

    def send_grade_notification(self, sender, password):
        subject = 'Wystawiona ocena'

        if 'MAILED' in self.status:
            print('Mail został wysłany')
            return

        body = f'Dzień Dobry {self.first_name},\n\n' \
               f'Wystawiłam ocenę {self.final_grade} z przedmiotu Podstawy Programowania Python. ' \
               f'Proszę o sprawdzenie, czy wszystko się zgadza.\n\n' \
               f'Pozdrawiam,\n\n' \
               f'Romuald Galileo'
        self.send_email(sender=sender, subject=subject, body=body, password=password)
        self.status = 'MAILED'

        print('Wiadomości email zostały wysłane.')


class MySortedList:
    list_of_students: list[Student]
    file_name: str

    def __init__(self, file_name):
        self.file_name = file_name
        self.list_of_students = []

        with open(self.file_name, 'r') as file:
            for line in file.readlines():
                line = line.strip().split(',')
                self.list_of_students.append(Student(email=line[0],
                                                     first_name=line[1],
                                                     last_name=line[2],
                                                     project_points=int(line[3]),
                                                     list_points=[int(points) for points in line[4:7]],
                                                     homework_points=[int(points) for points in line[7:17]],
                                                     final_grade=int(line[17]),
                                                     status=line[18]))

    def send_emails(self, sender, password):
        for student in self.list_of_students:
            student.send_grade_notification(sender, password)


students: MySortedList = MySortedList('/Users/marysiasurawska/Downloads/ocenystudenci')
print(students.list_of_students)

for student in students.list_of_students:
    student.grade_student()

