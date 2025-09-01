ANALIZA PODATKOV - PREHRANSKI DODATKI NA FUTUNATURA

Za seminarsko nalogo sem se odločila analizirati prehranske dodatke na spletni strani Futunatura. Ker sama uporabljam nekaj športnih prehranskih dodatkov, me je zanimalo, kako so organizirani na trgu in kakšne so cene.

STRUKTURA PROJEKTA:
- Raw_podatki -> mapa ki vsebuje vse html strani ki mi jih je uspelo prenesti iz spletne strani futunatura
- analiza_jupyter.ipynb -> jupyter notebook kjer sem naredila analizo podatkov in prikazala rezultate analize
- podatki_o_vseh_izdelkih.csv -> csv datoteka s podatki o izdelkih
- podatki_o_vseh_izdelkih.json -> json datoteka s podatki o izdelkih
- shranjevanje_podatkov.py -> datoteka ki shrani podatke iz spletne strani v mapo raw podatki v obliki html datotek
- README.md -> opis projekta in delovanja 

UGOTOVITVE:
- vse ugotovitve so podrobneje opisane v datoteki analiza_jupyter.ipynb

POGANJANJE KODE:

1. PRENOS PROJEKTA Z GITHUBA:
   - Odpri terminal/command prompt
   - Pojdi v mapo kjer zelis shraniti projekt (npr. Desktop)
   - Vnesi ukaz: git clone https://github.com/linacizman/seminarska_naloga_UVP
   - Projekt se bo prenesel v novo mapo

2. NAMESTITEV VIRTUALNEGA OKOLJA:
   - Odpri terminal v mapi s projektom
   - Ustvari virtualno okolje: python -m venv venv
   - Aktiviraj virtualno okolje:
     * Na Windows: venv\Scripts\activate
     * Na Mac/Linux: source venv/bin/activate
   - Ko je aktivno, bo v terminalu videti (venv) na zacetku vrstice

3. NAMESTITEV KNJIZNIC:
   Projekt uporablja naslednje knjiznice:
   - pandas (za delo s podatki)
   - matplotlib (za grafikone)
   - scikit-learn (za linearno regresijo)
   - scipy (za statistike)
   - beautifulsoup4 (za web scraping)
   - requests (za prenašanje spletnih strani)
   - jupyter (za notebook)
   - numpy (za numerične operacije)
   
   Namesti vse z ukazom:
   pip install pandas matplotlib scikit-learn scipy beautifulsoup4 requests jupyter numpy

4. ZAGON POSAMEZNIH DATOTEK:

   ZAGON WEB SCRAPINGA (priprava_podatkov.py):
   - Ta datoteka prenaša podatke s spletne strani Futunatura
   - Zaženi z: python priprava_podatkov.py
   - Ustvari mapo Raw_podatki z HTML datotekami
   - Ustvari CSV in JSON datoteki s podatki

   ZAGON SHRAJEVANJA (shranjevanje_podatkov.py):
   - Ta datoteka shrani HTML strani v mapo Raw_podatki
   - Zaženi z: python shranjevanje_podatkov.py
   - Preveri da imas internetno povezavo


TEŽAVE, KI SEM JIH IMELA:
- Podatki niso bili standardizirani: Nekateri izdelki imajo količino v gramih, drugi v kapsulah, tretji pa "3x 500g"
- Manjkajoči podatki: Nekateri izdelki nimajo vseh informacij

ZAKLJUČEK
- skozi projekt sem se naučila precej novih stvari in ugotovila kako dobro lahko s pomočjo orodji v pythonu beremo in analiziramo podatke ki so na voljo na 
  internetu in jih prikažemo v poročilu. To se mi zdi zelo koristno znanje in upam da ga bom imela še kdaj priložnost uporabiti.

