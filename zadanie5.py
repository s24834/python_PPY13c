import smtplib
from email.mime.text import MIMEText

# funkcja do wczytania danych z pliku
def load_data(file_path):
    students = []
    with open(file_path) as file_object:
        for line in file_object:
            data = line.split(',')
            data[-1] = data[-1].strip()
            student = {
                'email': data[0],
                'first_name': data[1],
                'last_name': data[2],
                'points': int(data[3])
            }
            if len(data) >= 5:
                student['grade'] = float(data[4])
            if len(data) >= 6:
                student['status'] = data[5]
            students.append(student)
    return students


print("load_data")
students = load_data('students1.txt')
for student in students:
    print(student)


# funkcja do zapisywania danych do pliku
def save_data(file_path, data: list[dict]):
    with open(file_path, 'w') as file_object:
        for student in data:
            file_object.write(','.join([str(v) for v in student.values()]) + '\n')


print("save_data")
save_data('test.txt', students)


# funkcja do dodawania nowego studenta
def add_student(data: list[dict], file_path):
    email: str = input('Podaj adres email: ')
    print([s['email'] for s in data])
    if email in [s['email'] for s in data]:
        print('Student o podanym adresie email już istnieje.')
        return
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    points = int(input('Podaj liczbę punktów z przedmiotu: '))
    status = ''
    grade = ''
    data.append({'first_name': first_name, 'last_name': last_name, 'points': points, 'status': status, 'grade': grade})
    save_data(file_path, data)
    print('Student dodany.')


print("add_data")
print(students)
add_student(students, "test.txt")


# funkcja do usuwania istniejącego studenta
def remove_student(data: list[dict], file_path):
    email: str = input('Podaj adres email studenta do usunięcia: ')
    if email not in [s['email'] for s in data]:
        print('Nie ma studenta o podanym adresie email.')
        return

    ind = -1
    for s in data:
        ind += 1
        if s['email'] == email:
            break

    data = data[:ind] + data[ind + 1:]

    save_data(file_path, data)
    print('Student usunięty.')


print("remove_students")
print(f"students: {students}")
remove_student(students, "copy.txt")


'''
    50 i mniej -2
    51 -60 pkt -3
    61 –70 pkt –3.5
    71 –80 pkt -4
    81 -90 pkt –4.5
    91 -100 pkt –5
'''


# funkcja do automatycznego wystawienia oceny
def grade_students(data: list[dict], file_path):
    for student_data in data:
        if 'status' not in student_data or student_data['status'] not in ['GRADED', 'MAILED']:
            points = int(student_data['points'])
            if points >= 91:
                grade = '5.0'
            elif points >= 81:
                grade = '4.5'
            elif points >= 71:
                grade = '4.0'
            elif points >= 61:
                grade = '3.5'
            elif points >= 51:
                grade = '3.0'
            else:
                grade = '2.0'
            student_data['status'] = 'GRADED'
            student_data['grade'] = grade
            print(f'Ocena wystawiona dla studenta o adresie email {student_data["email"]}.')
    save_data(file_path, data)


grade_students(students, "copy.txt")


# wysyłanie maila
def send_email(subject, body, sender: str, recipients: list[str], password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)

    smtp_server.sendmail(sender, recipients, msg.as_string())

    smtp_server.quit()


def send_grade_notification(data: list[dict], sender, password, file_path):
    subject = 'Wystawiona ocena'

    for student_data in data:
        if student_data['status'] != 'MAILED':
            to_email = student_data['email']
            body = f'Dzień Dobry {student_data["first_name"]},\n\n' \
                   f'Wystawiłam ocenę {student_data["grade"]} z przedmiotu Podstawy Programowania Python. ' \
                   f'Proszę o sprawdzenie, czy wszystko się zgadza.\n\n' \
                   f'Pozdrawiam,\n\n' \
                   f'Romuald Galileo'
            send_email(sender=sender, subject=subject, body=body, recipients=[to_email], password=password)
            student_data['status'] = 'MAILED'

    save_data(file_path, data)
    print('Wiadomości email zostały wysłane.')

