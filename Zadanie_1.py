wiek_studenta_1 = input("wproadz_wiek_1_studenta:")
wiek_studenta_2 = input("wprowadz_wiek_2_studenta:")

wiek_studenta_1 = int(wiek_studenta_1)
wiek_studenta_2 = int(wiek_studenta_2)

print(wiek_studenta_1)
print(wiek_studenta_2)

if(wiek_studenta_1 > wiek_studenta_2):
    tekst = "Pierwszy student jest starszy i ma" + str(wiek_studenta_1) + "lat(a)."
    print(tekst)
    
with open ("wiek_1_studenta.txt",'a') as plik: 
    plik.write(tekst)