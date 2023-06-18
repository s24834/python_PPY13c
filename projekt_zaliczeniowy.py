import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# ładowanie zbioru danych z podanego adresu URL i nadawanie kolumnom nazw
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
dataset = pd.read_csv(url, names=names)

# iteracja po wierszach zbioru danych i zamienianie wartości "?" na domyślne wartości dla odpowiednich kolumn
for i, row in dataset.iterrows():
    if row['workclass'] == ' ?':
        row['workclass'] = 'Private'
        dataset.at[i, 'workclass'] = row['workclass']
    if row['education'] == ' ?':
        row['education'] = 'Bachelors'
        dataset.at[i, 'education'] = row['education']
    if row['marital-status'] == ' ?':
        row['marital-status'] = 'Married-civ-spouse'
        dataset.at[i, 'marital-status'] = row['marital-status']
    if row['occupation'] == ' ?':
        row['occupation'] = 'Prof-specialty'
        dataset.at[i, 'occupation'] = row['occupation']
    if row['relationship'] == ' ?':
        row['relationship'] = 'Husband'
        dataset.at[i, 'relationship'] = row['relationship']
    if row['race'] == ' ?':
        row['race'] = 'White'
        dataset.at[i, 'race'] = row['race']
    if row['sex'] == ' ?':
        row['sex'] = 'Male'
        dataset.at[i, 'sex'] = row['sex']
    if row['native-country'] == ' ?':
        row['native-country'] = 'United-States'
        dataset.at[i, 'native-country'] = row['native-country']

# wstępne obróbki danych
# przetwarzanie danych: zamienianie znaków "?" na wartości NaN,
# a następnie usuwanie wierszy zawierających brakujące wartości
dataset = dataset.replace('?', np.nan)
dataset = dataset.dropna()

# zamiana etykiet " <=50K" i " >50K" na wartości liczbowe 0 i 1
dataset['income'] = dataset['income'].replace([' <=50K', ' >50K'], [0, 1])
dataset = pd.get_dummies(dataset, columns=['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country'])

# dzielenie zbioru danych na zbiór treningowy i testowy
X = dataset.drop('income', axis=1)
y = dataset['income']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# przetwarzanie etykiet zmiennych wynikowych y_train na wartości liczbowe
y_train = pd.to_numeric(y_train)

'''
    1. Wykorzystywać model uczenia maszynowego (klasyfikacja/regresja)
       przy użyciu wybranych danych innych niż Iris: https://archive.ics.uci.edu/ml/datasets.php
       Dokonywać Oceny modelu oraz umożliwiać predykcję/klasyfikację
       przy użyciu nowych danych - 10 pkt.
'''

# tworzenie modelu regresji logistycznej i trenowanie go na danych treningowych
model = LogisticRegression()
model.fit(X_train, y_train)

# ocena modelu na podstawie danych testowych, obliczając dokładność predykcji
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

'''
    4. Zapisywać i odczytywać model na dysk, aby nie trzeba było trenować modelu przy każdym uruchomieniu aplikacji
'''

# zapisanie wytrenowanego modelu do pliku "model.pkl" (dysku)
joblib.dump(model, 'model.pkl')

# wczytanie zapisanego wcześniej modelu z pliku "model.pkl" (na dysk)
model = joblib.load('model.pkl')

'''
    2. Posiadać Graficzny interfejs Użytkownika umożliwiający:
       trenowanie,
       testowanie,
       predykcję nowych danych,
       dodanie nowych danych,
       ponowne zbudowanie modelu- 10 pkt.
'''

# tworzenie interfejsu graficznego (biblioteka tkinter)
root = tk.Tk()
root.title("Adult Dataset Classifier")


# funkcja do otwierania plików CSV za pomocą okna dialogowego
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        table.delete(*table.get_children())
        for i, row in df.iterrows():
            table.insert("", "end", values=list(row))
    else:
        messagebox.showerror("Error", "Invalid file format. Please select a CSV file.")


# funkcja do przewidywania dochodu nowej osoby na podstawie wprowadzonych danych
def predict_income():
    age = int(age_entry.get())
    workclass = workclass_var.get()
    fnlwgt = int(fnlwgt_entry.get())
    education = education_var.get()
    education_num = int(education_num_entry.get())
    marital_status = marital_status_var.get()
    occupation = occupation_var.get()
    relationship = relationship_var.get()
    race = race_var.get()
    sex = sex_var.get()
    capital_gain = int(capital_gain_entry.get())
    capital_loss = int(capital_loss_entry.get())
    hours_per_week = int(hours_per_week_entry.get())
    native_country = native_country_var.get()

    # tworzenie ramek danych dla wszystkich możliwych kategorii
    data = {'age': [age],
            'workclass': [workclass],  # klasa robotnicza (pracująca)
            'fnlwgt': [fnlwgt],  # 'fnlwgt' = final weight, czyli ile ludzi ma taką samą listę cech (wg. spisu ludności)
            'education': [education],
            'education-num': [education_num],
            'marital-status': [marital_status],
            'occupation': [occupation],
            'relationship': [relationship],
            'race': [race],
            'sex': [sex],
            'capital-gain': [capital_gain],  # zysk kapitałowy
            'capital-loss': [capital_loss],  # strata kapitałowa
            'hours-per-week': [hours_per_week],
            'native-country': [native_country]}  # kraj rodzimy

    df = pd.DataFrame(data)

    # zastosowanie techniki one-hot encoding na ramkach danych
    # one-hot encoding to technika wykorzystywana do przekształcania zmiennych kategorycznych na postać numeryczną
    # utworzenie dodatkowych kolumn (binarnych) dla każdej kategorii w zmiennej kategorycznej
    # każda kolumna odpowiada jednej kategorii i przyjmuje wartość 1 (jeśli próbka należy do danej kategorii)
    # lub 0 w przeciwnym przypadku
    # zachowuje informację o przynależności do konkretnej kategorii
    df = pd.get_dummies(df, columns=['workclass', 'education', 'marital-status', 'occupation',
                                     'relationship', 'race', 'sex', 'native-country'])

    # zestaw ze sobą kolumny ramki danych predykcji z kolumnami ramki danych trenujących
    df = df.reindex(columns=X_train.columns, fill_value=0)

    # przewidywanie dochodu wykorzystując wytrenowany model
    income = model.predict(df)[0]

    if income == 0:
        income_label.config(text="<=50K")
    else:
        income_label.config(text=">50K")


# funkcja do dodawania nowych danych do zbioru
def add_data():
    age = int(age_entry.get())
    workclass = workclass_var.get()
    fnlwgt = int(fnlwgt_entry.get())
    education = education_var.get()
    education_num = int(education_num_entry.get())
    marital_status = marital_status_var.get()
    occupation = occupation_var.get()
    relationship = relationship_var.get()
    race = race_var.get()
    sex = sex_var.get()
    capital_gain = int(capital_gain_entry.get())
    capital_loss = int(capital_loss_entry.get())
    hours_per_week = int(hours_per_week_entry.get())
    native_country = native_country_var.get()
    income = int(income_var.get().replace('<=50K', '0').replace('>50K', '1'))
    data = {'age': age, 'workclass': workclass, 'fnlwgt': fnlwgt, 'education': education, 'education-num': education_num, 'marital-status': marital_status, 'occupation': occupation, 'relationship': relationship, 'race': race, 'sex': sex, 'capital-gain': capital_gain, 'capital-loss': capital_loss, 'hours-per-week': hours_per_week, 'native-country': native_country, 'income': income}
    df = pd.DataFrame(data, index=[0])
    conn = sqlite3.connect('data.db')
    df.to_sql('adult', conn, if_exists='append', index=False)
    conn.close()
    messagebox.showinfo("Success", "Data added successfully.")


'''
    3.Umożliwiać przeglądanie danych za pomocą tabelki- 5 pkt.
'''


# funkcja do wyświetlania danych w tabeli
def view_data():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * from adult", conn)
    table.delete(*table.get_children())
    for i, row in df.iterrows():
        table.insert("", "end", values=list(row))
    conn.close()


'''
    5. Wizualizować dane na wykresie- 5 pkt.
'''


# funkcja do tworzenia wykresu
def plot_data():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * from adult", conn)
    sns.pairplot(df, hue='income')
    plt.show()
    conn.close()


'''
    6. Przechowywać dane w bazie SQLite(zapis,odczyt)-5pkt.
'''


# funkcja do dodawania danych do bazy danych
def add_data_to_database():
    # nawiązanie połączenia z bazą danych
    conn = sqlite3.connect('data.db')

    # sprawdzanie, czy tabela 'adult' istnieje już w bazie danych
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='adult'")
    table_exists = cursor.fetchall()

    if not table_exists:
        # jeżeli tabela 'adult' nie istnieje, stwórz ją w bazie danych
        dataset.to_sql('adult', conn, if_exists='replace', index=False)
        messagebox.showinfo("Success", "Data added successfully.")
    else:
        # jeżeli tabela 'adult' już istnieje, wyślij komunikat do użytkownika z zapytaniem, czy chce ją zastąpić
        message = "The 'adult' table already exists in the database.\nDo you want to replace the existing data?"
        response = messagebox.askyesno("Warning", message)

        if response == tk.YES:
            # jeżeli użytkownik zdecyduje się na zastąpienie tabeli 'adult' nową,
            # to usuń istniejącą i stwórz nową
            cursor.execute("DROP TABLE IF EXISTS adult")
            dataset.to_sql('adult', conn, if_exists='replace', index=False)
            messagebox.showinfo("Success", "Data replaced successfully.")
        else:
            # jeżeli użytkownik nie zdecyduje się na zastąpienie tabeli 'adult' nową, nie dokonuj zmian
            messagebox.showinfo("Info", "No changes were made.")

    # zamknięcie połączenia z bazą danych
    conn.close()


# zapisywanie danych do bazy danych
add_data_to_database()

# tworzenie paska menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# tworzenie menu "File" z opcją "Open" do otwierania plików
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)

# tworzenie menu "Data" z opcjami "View" i "Plot" do wyświetlania danych i tworzenia wykresu
data_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Data", menu=data_menu)
data_menu.add_command(label="View", command=view_data)
data_menu.add_command(label="Plot", command=plot_data)

# tworzenie ramki dla pól wejściowych w interfejsie graficznym
input_frame = tk.Frame(root)
input_frame.pack()

# tworzenie etykiet i pól wejściowych dla danych osobowych
age_label = tk.Label(input_frame, text="Age:")
age_label.grid(row=0, column=0)
age_entry = tk.Entry(input_frame)
age_entry.grid(row=0, column=1)

workclass_label = tk.Label(input_frame, text="Workclass:")
workclass_label.grid(row=1, column=0)
workclass_var = tk.StringVar()
workclass_options = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
workclass_dropdown = tk.OptionMenu(input_frame, workclass_var, *workclass_options)
workclass_dropdown.grid(row=1, column=1)

fnlwgt_label = tk.Label(input_frame, text="Fnlwgt:")
fnlwgt_label.grid(row=2, column=0)
fnlwgt_entry = tk.Entry(input_frame)
fnlwgt_entry.grid(row=2, column=1)

education_label = tk.Label(input_frame, text="Education:")
education_label.grid(row=3, column=0)
education_var = tk.StringVar()
education_options = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
education_dropdown = tk.OptionMenu(input_frame, education_var, *education_options)
education_dropdown.grid(row=3, column=1)

education_num_label = tk.Label(input_frame, text="Education-num:")
education_num_label.grid(row=4, column=0)
education_num_entry = tk.Entry(input_frame)
education_num_entry.grid(row=4, column=1)

marital_status_label = tk.Label(input_frame, text="Marital-status:")
marital_status_label.grid(row=5, column=0)
marital_status_var = tk.StringVar()
marital_status_options = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
marital_status_dropdown = tk.OptionMenu(input_frame, marital_status_var, *marital_status_options)
marital_status_dropdown.grid(row=5, column=1)

occupation_label = tk.Label(input_frame, text="Occupation:")
occupation_label.grid(row=6, column=0)
occupation_var = tk.StringVar()
occupation_options = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
occupation_dropdown = tk.OptionMenu(input_frame, occupation_var, *occupation_options)
occupation_dropdown.grid(row=6, column=1)

relationship_label = tk.Label(input_frame, text="Relationship:")
relationship_label.grid(row=7, column=0)
relationship_var = tk.StringVar()
relationship_options = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
relationship_dropdown = tk.OptionMenu(input_frame, relationship_var, *relationship_options)
relationship_dropdown.grid(row=7, column=1)

race_label = tk.Label(input_frame, text="Race:")
race_label.grid(row=8, column=0)
race_var = tk.StringVar()
race_options = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
race_dropdown = tk.OptionMenu(input_frame, race_var, *race_options)
race_dropdown.grid(row=8, column=1)

sex_label = tk.Label(input_frame, text="Sex:")
sex_label.grid(row=9, column=0)
sex_var = tk.StringVar()
sex_options = ['Male', 'Female']
sex_dropdown = tk.OptionMenu(input_frame, sex_var, *sex_options)
sex_dropdown.grid(row=9, column=1)

capital_gain_label = tk.Label(input_frame, text="Capital-gain:")
capital_gain_label.grid(row=10, column=0)
capital_gain_entry = tk.Entry(input_frame)
capital_gain_entry.grid(row=10, column=1)

capital_loss_label = tk.Label(input_frame, text="Capital-loss:")
capital_loss_label.grid(row=11, column=0)
capital_loss_entry = tk.Entry(input_frame)
capital_loss_entry.grid(row=11, column=1)

hours_per_week_label = tk.Label(input_frame, text="Hours-per-week:")
hours_per_week_label.grid(row=12, column=0)
hours_per_week_entry = tk.Entry(input_frame)
hours_per_week_entry.grid(row=12, column=1)

native_country_label = tk.Label(input_frame, text="Native-country:")
native_country_label.grid(row=13, column=0)
native_country_var = tk.StringVar()
native_country_options = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']
native_country_dropdown = tk.OptionMenu(input_frame, native_country_var, *native_country_options)
native_country_dropdown.grid(row=13, column=1)

income_label = tk.Label(input_frame, text="Income (fill only if adding data)")
income_label.grid(row=14, column=0)
income_var = tk.StringVar()
income_options = ['<=50K', '>50K']
income_dropdown = tk.OptionMenu(input_frame, income_var, *income_options)
income_dropdown.grid(row=14, column=1)

# przyciski
predict_button = tk.Button(root, text="Predict", command=predict_income)
predict_button.pack()

add_button = tk.Button(root, text="Add Data", command=add_data)
add_button.pack()

# tworzenie ramki do tabeli
table_frame = tk.Frame(root)
table_frame.pack()

# tworzenie tabeli
table = tk.ttk.Treeview(table_frame, columns=names, show='headings')
for name in names:
    table.heading(name, text=name)
table.pack(side='left', fill='both', expand=True)

root.mainloop()
