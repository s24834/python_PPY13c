url = input("podaj adres strony")

import requests # moduł requests pozwala na wysyłanie żądań HTTP wykorzystując Pythona
versions_dates = ["20231410", "20221410", "20211410"] # lista z datami archiwalnymi

for date in versions_dates:
    j = requests.get(f"https://archive.org/wayback/available?url={url}&timestamp={date}").json() # słownik
    archive = j["archived_snapshots"]["closest"]["url"] # pozyskanie url potrzebnego do parametru metody .get()
    browser = requests.get(archive).text # text pozyskuje zawartość request'owanego pliku
    with open(f"{date}.html", "w") as b: # metoda open() otwiera plik, na którym będę pracować; open() przyjmuje 3 parametry [nazwa] [mode, czyli w=write, r=read, a=append] [encoding]
        # with open() działa tak samo jak open(), z tą różnicą, że with open() sam zamyka plik (bez metody nazwa_pliku.close())
        b.write(browser) # write wypisuje do podanego pliku podany w argumencie text (z opcją "w" całą zawartość pliku usuwa i wstawia dany, nowy tekst)

