### Zadatak 1. Napiši funkciju koji obračunava zaradu radnika. Radnici koji rade više od 40 sati nedeljno su
### plaćeni 1.5 puta više nego što bi bili plaćeni da rade do 40 sati nedeljno. Broj radnih sati po danima
### završene radne nedelje se učitava iz fajla. Funkcija kao parametar prima putanju do fajla sa radnim
### satima i cenu radnog sata i ispisuje imena i zarade radnika.
### Primer izvrašavanja programa:
### Za fajl radnici.txt
### pera|8|9|7|8|9
### jova|8|8|7|8|7
### steva|8|8|9|8|7
### rezultat poziva funkcije treba da bude:
### >>> racunanjeZarade("radnici.txt",1000)
### ime: pera
### zarada: 61500.0
### ime: jova
### zarada: 38000
### ime: steva
### zarada: 40000
def racunanjeZarade(putanja, cena):
    with open(putanja) as f:
        for linija in f:
            delovi = linija.strip().split("|")
            ime = delovi[0]
            sati = [int(x) for x in delovi[1:]]
            ukupno_sati = sum(sati)
            if ukupno_sati > 40:
                zarada = ukupno_sati * cena * 1.5
            else:
                zarada = ukupno_sati * cena
            print("ime: " + ime)
            print("zarada: " + str(zarada))

racunanjeZarade("radnici.txt", 1000)