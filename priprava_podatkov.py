import bs4
import os
import json
import csv

def main():
    vsi_izdelki = najdi_izdelke_na_strani()
    podatki_o_vseh_izdelki = najdi_informacije_izdelkov(vsi_izdelki)

    with open('podatki_o_vseh_izdelki.json', 'w', encoding='utf-8') as f:
        json.dump(podatki_o_vseh_izdelki, f, ensure_ascii=False, indent=2)

    with open('podatki_o_vseh_izdelki.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Ime", "Znamka", "Količina", "Cena", "Originalna cena", "Popust", "Prednosti"])
        
        for oglas in podatki_o_vseh_izdelki:
            writer.writerow([
                oglas.get("ime", ""),
                oglas.get("znamka", ""),
                oglas.get("kolicina ", ""),
                oglas.get("cena", ""),
                oglas.get("originalna_cena", ""),
                oglas.get("popust", ""),
                oglas.get("prednosti", ""),
            ])

def najdi_izdelke_na_strani():
    vse_strani = os.listdir("Raw_podatki")
    vsi_izdelki = []
    for stran in vse_strani:
        with open("Raw_podatki/" + stran, "r", encoding="utf-8") as f:
            stran = f.read()
        juha = bs4.BeautifulSoup(stran, "html.parser")
        izdelki = juha.find_all("div", class_="item item_box")
        vsi_izdelki.extend(izdelki)
    return vsi_izdelki

def najdi_informacije_izdelkov(vsi_izdelki):

    podatki_o_vseh_izdelki = []
    for izdelek in vsi_izdelki:
        try:
            ime = izdelek.find("h3").get_text(strip=True)
            znamka = izdelek.find("div", class_="p_info_txt p_info_color").get_text(strip=True)
            kolicina = izdelek.find_all("div", class_="p_info_txt")[-1].get_text(strip=True)
            cena = izdelek.find("span", class_="combo_price").get_text(strip=True)
            originalna_cena = izdelek.find("span", class_="combo_full_price")
            originalna_cena = originalna_cena.get_text(strip=True) if originalna_cena else None
            popust = izdelek.find("div", class_="sale_box")
            popust = popust.get_text(strip=True) if popust else None
            prednosti = [li.get_text(strip=True) for li in izdelek.select(".advantages_wrap li")]

            podatki_o_izdelku = {
                "ime": ime,
                "znamka": znamka,
                "kolicina": kolicina,
                "cena": cena,
                "originalna_cena": originalna_cena,
                "popust": popust,
                "prednosti": prednosti
            }
            podatki_o_vseh_izdelki.append(podatki_o_izdelku)
        
        except Exception as e:
            print("Prišlo je do napake pri iskanju informacij o izdelku")
            continue
    return podatki_o_vseh_izdelki

if __name__ == "__main__":
    main()