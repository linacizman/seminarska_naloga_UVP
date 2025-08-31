import requests
import bs4
import os

#url na katerem je dostopna stran z izdelki brez informacije o strani saj jo spreminjamo v for zanki
url = "https://www.futunatura.si/sport-menu?page="

#s for zanko gremo po vseh straneh in shranjujemo vsebino vsake strani v mapo Raw_podatki
#uporabimo try except in javimo če pri branju pride do napake
for i in range(1, 34):
    try:
        response = requests.get(url + str(i))
        juha = bs4.BeautifulSoup(response.text, "html.parser")
        if not os.path.exists("Raw_podatki"):
            os.makedirs("Raw_podatki")
        with open("Raw_podatki/stran" + str(i) + ".html", "w", encoding="utf-8") as f:
            f.write(str(juha))
    except Exception as e:
        print("Prislo je do napake pri branju strani " + str(i))
        continue