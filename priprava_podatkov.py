import bs4
import os
import json
import csv

def main(): # galvna funkcija ki se izvede ob zagonu programa
    vsi_izdelki = najdi_izdelke_na_strani()
    podatki_o_vseh_izdelki = najdi_informacije_izdelkov(vsi_izdelki)

    with open('podatki_o_vseh_izdelki.json', 'w', encoding='utf-8') as f: # podatke shranimo v json datoteko
        json.dump(podatki_o_vseh_izdelki, f, ensure_ascii=False, indent=2)

    with open('podatki_o_vseh_izdelki.csv', 'w', newline='', encoding='utf-8') as f: # podatke shranimo v csv datoteko
        writer = csv.writer(f)
        writer.writerow(["Ime", "Znamka", "Količina", "Cena", "Originalna cena", "Popust", "Prednosti"])
        
        for oglas in podatki_o_vseh_izdelki:
            writer.writerow([
                oglas.get("ime", ""),
                oglas.get("znamka", ""),
                oglas.get("kolicina", ""),
                oglas.get("cena", ""),
                oglas.get("originalna_cena", ""),
                oglas.get("popust", ""),
                oglas.get("prednosti", ""),
            ])

def najdi_izdelke_na_strani(): # funkcija ki najde vse izdelke na strani
    vse_strani = os.listdir("Raw_podatki")
    vsi_izdelki = []
    for stran in vse_strani:
        with open("Raw_podatki/" + stran, "r", encoding="utf-8") as f:
            stran = f.read()
        juha = bs4.BeautifulSoup(stran, "html.parser")
        izdelki = juha.find_all("div", class_="item item_box") # posamezni izdelki so v tagu div z class_ item item_box
        vsi_izdelki.extend(izdelki) #izdelke ki jih najdemo na strani dodamo v seznam vsi_izdelki
    return vsi_izdelki #vrnemo seznam vsi_izdelki na vseh straneh

def najdi_informacije_izdelkov(vsi_izdelki): # funkcija ki najde informacije o posameznih izdelkih

    podatki_o_vseh_izdelki = []
    for izdelek in vsi_izdelki:
        try: # iz posameznega izdelka najdemo informacije o imenu, znamki, količini, ceni, originalni ceni, popustu in prednostih
            ime = izdelek.find("h3").get_text(strip=True)
            znamka = izdelek.find("div", class_="p_info_txt p_info_color").get_text(strip=True)
            kolicina = izdelek.find_all("div", class_="p_info_txt")[-1].get_text(strip=True)
            cena = izdelek.find("span", class_="combo_price").get_text(strip=True)
            originalna_cena = izdelek.find("span", class_="combo_full_price")
            originalna_cena = originalna_cena.get_text(strip=True) if originalna_cena else None
            popust = izdelek.find("div", class_="sale_box")
            popust = popust.get_text(strip=True) if popust else None
            prednosti = [li.get_text(strip=True) for li in izdelek.select(".advantages_wrap li")]

            podatki_o_izdelku = { # podatke o izdelku shranimo v slovar
                "ime": ime,
                "znamka": znamka,
                "kolicina": kolicina,
                "cena": cena,
                "originalna_cena": originalna_cena,
                "popust": popust,
                "prednosti": prednosti
            }
            podatki_o_vseh_izdelki.append(podatki_o_izdelku) # podatke o izdelku ki so shranjeni kot slovar dodamo v seznam podatki_o_vseh_izdelki
        
        except Exception as e:
            print("Prišlo je do napake pri iskanju informacij o izdelku")
            continue
    return podatki_o_vseh_izdelki # vrnemo seznam podatki_o_vseh_izdelki ki vsebuje vse podatke o izdelkih v obliki slovarjev kjer je vsak izdelek v svojem slovarju

if __name__ == "__main__": # glavna funkcija ki se izvede ob zagonu programa
    main()