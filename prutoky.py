import csv

with open ("sample_vstup.csv", encoding="utf-8") as vstup, open("vystup_7dni.csv","w", encoding="utf-8", newline="") as tyzdnovy_vystup, open("vystup_rok.csv","w", encoding="utf-8", newline="") as rocny_vystup:
    reader = csv.reader(vstup, delimiter = ",")
    writer_7 = csv.writer(tyzdnovy_vystup)
    writer_365 = csv.writer(rocny_vystup)

    zasobnik_tyzden = []
    zasobnik_rok = []                      ### Zasobniky, do ktoreho sa volaju priemery v priebehu 7 dni a celeho roka
    cislo_riadku = 0                       ### Pocitadlo riadkov, pomaha si s premennou prvy_riadok_tyzdna; relevantne len pre pocitanie dnov v tyzdni
    aktualny_rok = 0                       ### Premenna, do ktorej sa na prvom riadku vo vstupe ulozi rok, vychadza z nej cyklus
    prvy_riadok_tyzdna = 0                 ### Premenna, ktora zaistuje, ze sa do riadka ulozi prvy den z kazdeho tyzdna
    prvy_riadok_roku = 0                   ### Premenna, ktora zaistuje, ze sa do riadka ulozi prvy den vo vstupe a nasledne prvy den z kazdeho roku
    priemer_tyzdna = 0                     ### Aritmeticky priemer prietokov za 7 dni
    priemer_roku = 0                       ### Aritmeticky priemer prietokov za rok, resp. od prveho riadku vstupu do konca roka 
    max_prietok = 0
    min_prietok = 0

    for riadok in reader:
            
        if len(riadok) != 6:
            raise Exception("POZOR: Vstupne data nemaju pozadovany pocet stlpcov (6)")

        cislo_riadku += 1

        if max_prietok == 0 and min_prietok == 0:   ### Priprava slice riadku do premennych
            max_prietok = riadok[2:6]
            min_prietok = riadok[2:6]
        
        if float(riadok[5]) > float(max_prietok[3]):    ### Vyrez riadku sa nahradi v momente, ked sa najde vacsi prietok
            max_prietok = riadok[2:6]

        if float(riadok[5]) < float(min_prietok[3]):    ### Vyrez riadku sa nahradi v momente, ked sa najde mensi prietok
            min_prietok = riadok[2:6]

        if aktualny_rok == 0:                       ### Nastavi aktualny rok na rok prveho riadku vstupu
            aktualny_rok = int(riadok[2]) 
        
        if cislo_riadku % 7 == 1:                   ### Prvy riadok zo vstupu sa ulozi do premennej, ktora sa meni kazdych 7 dni
            prvy_riadok_tyzdna = riadok        
        
        if prvy_riadok_roku == 0:                   ### Prvy riadok zo vstupu sa ulozi do premennej, ktora sa meni kazdou zmenou roka v stlpci [2]
            prvy_riadok_roku = riadok              
        
        zasobnik_tyzden.append(float(riadok[5]))
        zasobnik_rok.append(float(riadok[5]))       ### Volanie prietokov do dvoch zasobnikov, dokym nie je stanovene inak

        if len(zasobnik_tyzden) == 7:
            priemer_tyzdna = (sum(zasobnik_tyzden))/len(zasobnik_tyzden)
            prvy_riadok_tyzdna[5] = ("{0:.4f}".format(priemer_tyzdna))        ### Zaistuje vypisanie priemerov na 4 desatinne miesta
            writer_7.writerow(prvy_riadok_tyzdna)
            zasobnik_tyzden.clear()                                           ### Vyprazdnenie zasobnika po vypocitani priemeru z tyzdna
        
        if int(riadok[2]) != aktualny_rok:                                    ### Vyhodnotenie zasobnika, ked sa zmeni rok
            priemer_roku = (sum(zasobnik_rok))/len(zasobnik_rok)
            prvy_riadok_roku[5] = ("{0:.4f}".format(priemer_roku))            ### Formatovanie na 4 desatinne miesta
            writer_365.writerow(prvy_riadok_roku)
            aktualny_rok = int(riadok[2])                                   
            prvy_riadok_roku = riadok                                         
            zasobnik_rok.clear()                                              ### Vyprazdnenie zasobnika po vypocitani priemeru z roku
    
    if len(zasobnik_tyzden) != 0:                                             ### Pokial vstup nie je delitelny 7, vypriemeruje sa zvysok zasobnika a prida sa k prvemu dnu nasledujuceho tyzdna
        priemer_tyzdna = (sum(zasobnik_tyzden))/len(zasobnik_tyzden) 
        prvy_riadok_tyzdna[5] = ("{0:.4f}".format(priemer_tyzdna))  
        writer_7.writerow(prvy_riadok_tyzdna)
        zasobnik_tyzden.clear()
    
    if len(zasobnik_rok) != 0:                                                ### Vyhodnotenie rocneho zasobnika s dnami navyse
        priemer_roku = (sum(zasobnik_rok))/len(zasobnik_rok) 
        prvy_riadok_roku[5] = ("{0:.4f}".format(priemer_roku))       
        writer_365.writerow(prvy_riadok_roku)
        zasobnik_rok.clear()

    max_prietok[3] = ("{0:.4f}".format(float(max_prietok[3])))
    min_prietok[3] = ("{0:.4f}".format(float(min_prietok[3])))

    print("Hotovo. Sedemdnove priemery prietokov sa nachadzaju vo vystup_7dni.csv, rocne priemery prietokov sa nachadzaju vo vystup_rok.csv.")
    print(f"Minimalny denny prietok bol dna {int(min_prietok[2])}. {int(min_prietok[1])}. {int(min_prietok[0])} o hodnote {min_prietok[3]}.")
    print(f"Maximalny denny prietok bol dna {int(max_prietok[2])}. {int(max_prietok[1])}. {int(max_prietok[0])} o hodnote {max_prietok[3]}.")