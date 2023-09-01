### Zadatak 5. Dadilja naplaćuje 150din po satu čuvanja dece do 9 sati uveče, a 100din po satu čuvanja dece
### posle 9 sati uveče. Napiši funkciju koja kao parametre prima vreme kada dadilja počinje da čuva deci i
### kada završava učuvanje dece, a vraća poruku o zaradi koja treba se isplati. Vreme je zadato u formatu
### hh:mm, a pretpostavlja se da se čuvanje dece odvija u periodu od 24h.
### Primer izvršavanja programa:
### >>> print(dadilja('18:35','22:50'))
### zarada dadilje je 546 din
def dadilja(pocetak, kraj):
    pocetak_sati, pocetak_minuti = map(int, pocetak.split(':'))
    kraj_sati, kraj_minuti = map(int, kraj.split(':'))
    ukupno_minuta = (kraj_sati * 60 + kraj_minuti) - (pocetak_sati * 60 + pocetak_minuti)
    pre_9_sati = min(60 * (21 - pocetak_sati) + (60 - pocetak_minuti), ukupno_minuta)
    posle_9_sati = max(ukupno_minuta - pre_9_sati, 0)
    zarada = (pre_9_sati / 60) * 150 + (posle_9_sati / 60) * 100
    return "Zarada dadilje je {} din".format(int(zarada))

print(dadilja('18:35','22:50'))