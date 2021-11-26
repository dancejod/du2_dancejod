import csv

with open ("vstup.csv", encoding="utf-8") as vstup, open("sample_vystup.csv","w", encoding="utf-8", newline="") as tyzdnovy_vystup, open("sample_rocny_vystup.csv","w", encoding="utf-8", newline="") as rocny_vystup:
    reader = csv.reader(vstup, delimiter = ",")
    writer_7 = csv.writer(tyzdnovy_vystup)
    writer_365 = csv.writer(rocny_vystup)

    zasobnik = []                          ### Zasobnik, do ktoreho sa volaju priemery v priebehu 7 dni
    cislo_riadku = 0                       ### Pocitadlo riadkov, pomaha si s premennou prvy_riadok
    prvy_riadok = 1                        ### Premenna, ktora zaistuje, ze sa do riadka ulozi prvy den z kazdeho tyzdna
    priemer = 0                        
    
    # 7 dni

    '''''
    for riadok in reader:
        cislo_riadku += 1 
        
        if cislo_riadku % 7 == 1:
            prvy_riadok = riadok            ### Prvy riadok z tyzdna sa ulozi do premennej, v ktorej sa uz len modifikuje priemerny prietok

        zasobnik.append(float(riadok[5]))
           
        if len(zasobnik) == 7:
            priemer = (sum(zasobnik))/len(zasobnik)
            prvy_riadok[5] = ("{0:.4f}".format(priemer))        ### Zaistuje vypisanie priemerov na 4 desatinne miesta
            writer_7.writerow(prvy_riadok)
            zasobnik.clear()                    ### Vyprazdnenie zasobnika po vypocitani priemeru z tyzdna

    if len(zasobnik) != 0:                      ### Pokial vstup nie je delitelny 7, vypriemeruje sa zvysok zasobnika a prida sa k prvemu dnu nasledujuceho tyzdna
        priemer = (sum(zasobnik))/len(zasobnik) 
        prvy_riadok[5] = ("{0:.4f}".format(priemer))       
        writer_7.writerow(prvy_riadok)
        zasobnik.clear()
    
    '''

    # Rocny priemer

    prvy_riadok_roku = 1
    aktualny_rok = 0
    Prvy_den = 0
    Prvy_mesiac = 0                           ### Konstanty, ktore sa vyuziju na spravne pocita

    for riadok in reader:

        if aktualny_rok == 0:
            aktualny_rok = int(riadok[2])
            Prvy_mesiac = int(riadok[3])
            Prvy_den = int(riadok[4])           
        
        if prvy_riadok_roku == 1:
            prvy_riadok_roku = riadok               ### Ulozi prvy riadok vo vstupe

        zasobnik.append(float(riadok[5]))           ### Vola do zasobnika, kym sa nezastavi podla dalsej podmienky

        if int(riadok[2]) != aktualny_rok and int(riadok[3]) == Prvy_mesiac and int(riadok[4]) == Prvy_den:         ### Vyhodnotenie zasobnika s ohladom na priestupne roky
            priemer = (sum(zasobnik))/len(zasobnik)
            prvy_riadok_roku[5] = ("{0:.4f}".format(priemer))        ### Formatovanie na 4 desatinne miesta
            writer_365.writerow(prvy_riadok_roku)
            aktualny_rok = int(riadok[2])        
            prvy_riadok_roku = riadok                                ### Prepisanie vystupneho riadku na nasledujuci rok
            zasobnik.clear()

    if len(zasobnik) != 0:                                          ### Vyhodnotenie zasobnika s dnami navyse
        priemer = (sum(zasobnik))/len(zasobnik) 
        prvy_riadok_roku[5] = ("{0:.4f}".format(priemer))       
        writer_365.writerow(prvy_riadok_roku)
        zasobnik.clear()