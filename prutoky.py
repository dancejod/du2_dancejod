import csv

with open ("sample_vstup.csv", encoding="utf-8") as csvinfile, open("sample_vystup.csv","w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer = csv.writer(csvoutfile)

    zasobnik = []
    cislo_riadku = 0

    for riadok in reader:
        cislo_riadku += 1 
        priemer = 0
        if cislo_riadku % 7 == 1:
            writer.writerow([riadok])
            zasobnik.clear()
        else:
            zasobnik.append(riadok[5])
            if len(zasobnik) == 7:
                priemer = sum(zasobnik)
                riadok[5] = priemer

    print(zasobnik)
