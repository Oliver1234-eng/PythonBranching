### Zadatak 3. Indeks telesne mase se računa po sledećoj formuli BMI = m / h2 u kojoj je m masa u
### kilogramima, a h visina u metrima. U tabeli je data preporučena klasifikacija indeksa telesne mase:
### BMI Klasifikacija
### < 18,5 Pothranjenost
### 18,5 - 25 Idealna telesna težina
### 25 - 30 Preterana telesna težina
### > 30 Gojaznost
### Napiši funkciju koja prima težinu u kilogramima i visinu, a vraća kategoriju iz klasifikacije BMI.
### Primer izvršavanja programa:
### >>> print(indeksTelesneMase(55,1.8))
### 'pothranjenost'
### >>> print(indeksTelesneMase(75,1.8))
### 'idealna telesna tezina'
### >>> print(indeksTelesneMase(81,1.8))
### 'preterana telesna tezina'
### >>> print(indeksTelesneMase(120,1.8))
### 'gojaznost'
def indeksTelesneMase(tezina, visina):
    bmi = tezina / (visina ** 2)
    if bmi < 18.5:
        return 'pothranjenost'
    elif bmi >= 18.5 and bmi < 25:
        return 'idealna telesna tezina'
    elif bmi >= 25 and bmi < 30:
        return 'preterana telesna tezina'
    else:
        return 'gojaznost'

print(indeksTelesneMase(55, 1.8))

print(indeksTelesneMase(75, 1.8))

print(indeksTelesneMase(81, 1.8))

print(indeksTelesneMase(120, 1.8))



