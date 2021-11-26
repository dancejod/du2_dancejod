import csv

with open ("sample_vstup.csv", encoding="utf-8") as csvinfile, open("sample_vystup.csv","w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer = csv.writer(csvoutfile)

    zasobnik = []
    cislo_riadku = 0
    prvy_riadok = 1

    for riadok in reader:
        cislo_riadku += 1 
        priemer = 0
        if cislo_riadku % 7 == 1 or cislo_riadku == 1:
            prvy_riadok = riadok

        zasobnik.append(float(riadok[5]))
           
        if len(zasobnik) == 7:
            print(zasobnik)
            priemer = round((sum(zasobnik)),4)
            prvy_riadok[5] = priemer
            writer.writerow([prvy_riadok])
            zasobnik.clear()        
        #else:
            
