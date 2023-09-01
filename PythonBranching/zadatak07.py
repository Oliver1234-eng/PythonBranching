### Zadatak 7. Formula za izračunavanje datuma na koji pada uskrs u Gregorijanskom kalendaru data u
### prethodnom zadatku važi za sve godine od 1900 do 2099, osim za 1954., 1981., 2049. i 2076. Za te
### godine ova formula daje rezultat koji je nedelju dana kasnije nego što treba. Modifikuj zadatak 6 tako da
### važi za sve godine od 1900 do 2099.
def uskrs(year):
  if year < 1900 or year > 2099:
    return 'Godina nije u predviđenom opsegu'
  else:
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        a = year % 19
        d = (19 * a + 24) % 30
        d = d + 7
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    datum = 22 + d + e
    if datum > 31:
      return 'Uskrs je {} aprila {} godine.'.format(datum - 31, year)
    else:
      return 'Uskrs je {} marta {} godine.'.format(datum, year)

print(uskrs(1994))
print(uskrs(2011))
print(uskrs(1962))
print(uskrs(2049))