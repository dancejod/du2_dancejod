import csv

with open ("sample_vstup.csv", encoding="utf-8") as csvinfile, open("sample_vystup.csv","w", encoding="utf-8", newline="") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer = csv.writer(csvoutfile)

    zasobnik = []                          ### Zasobnik, do ktoreho sa volaju priemery v priebehu 7 dni
    cislo_riadku = 0                       ### Pocitadlo riadkov, pomaha si s premennou prvy_riadok
    prvy_riadok = 1                        ### Premenna, ktora zaistuje, ze sa do riadka ulozi prvy den z kazdeho tyzdna
    priemer = 0                        
    
    for riadok in reader:
        cislo_riadku += 1 
        
        if cislo_riadku % 7 == 1:
            prvy_riadok = riadok            ### Prvy riadok z tyzdna sa ulozi do premennej, v ktorej sa uz len modifikuje priemerny prietok

        zasobnik.append(float(riadok[5].strip()))
           
        if len(zasobnik) == 7:
            priemer = (sum(zasobnik))/7
            prvy_riadok[5] = ("{0:.4f}".format(priemer))        ### Zaistuje vypisanie priemerov na 4 desatinne miesta
            writer.writerow(prvy_riadok)
            zasobnik.clear()                    ### Vyprazdnenie zasobnika po vypocitani priemeru z tyzdna
        #else:
            
