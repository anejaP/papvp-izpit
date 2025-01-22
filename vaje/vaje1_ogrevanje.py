import pandas


#1.naloga
def papajscina(besedilo):
    novo = ''
    if besedilo == '':
        return ''
    for crka in besedilo:
        if crka in 'aeiouAEIOU':
            novo += crka + 'p' + crka
        else:
            novo += crka
    return novo

print(papajscina(''))
print(papajscina('a'))
print(papajscina('A'))
print(papajscina('t'))
print(papajscina('beseda'))
print(papajscina('pikapolonica'))
print(papajscina('popotovanje'))
print(papajscina('stepena smetana'))
print(papajscina('Tole je pa kar cela poved.'))


#2.naloga
def vmesne_vsote(podatki):
    nov = []
    vsota = 0
    if podatki == []:
        return []
    for i in range(len(podatki)):
        if podatki[i] <= 0:
            vsota = vsota
            nov.append(vsota)
        else:
            vsota += podatki[i]
            nov.append(vsota)
    return nov

print(vmesne_vsote([1, 1, 1, 1, 1]))
print(vmesne_vsote([1, 2, 3, 4, 5]))
print(vmesne_vsote([]))
print(vmesne_vsote([42]))
print(vmesne_vsote([1, 2, 3, -1, 5]))



#3.naloga
def unija_slovarjev(slovarji):
    nov_slovar = {}
    for slovar in slovarji:
        for kljuc, vrednost in slovar.items():
            if kljuc not in nov_slovar:
                nov_slovar[kljuc] = []  # Ustvari nov seznam, če ključ še ne obstaja
            nov_slovar[kljuc].append(vrednost)
    return nov_slovar

print(unija_slovarjev([{1: 2, 5: 0}, {2: 3, 5: 6, 7: 3}, {2: 3, 8: 1, 5: 4}]))



#4.naloga
def nagrajenci(redovalnica):
    povprecja = {}
    for vpisna, ocene in redovalnica.items():
        if len(ocene) == 0:
            break
        povp = round(sum(ocene) / len(ocene),1)
        povprecja[vpisna] = povp
    najvisje_povprecje = max(povprecja.values())
    nagrajenci = []
    for vpisna, povp in povprecja.items():
        if povp == najvisje_povprecje:
            nagrajenci.append(vpisna)
    return nagrajenci

redovalnica = {
    "12111111": [1, 2, 1, 2], 
    "12222222": [8, 8, 8, 8], 
    "12333333": [5, 10], 
    "12444444": [6, 10, 6, 10, 6, 10], 
    "12555555": [8],
    "12666666": [],
    "12777777": [6, 7, 8, 5],
    "12888888": [9, 6, 10, 6, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, \
                 8, 8, 9, 9, 7, 8]
}
print(nagrajenci(redovalnica))



#5.naloga