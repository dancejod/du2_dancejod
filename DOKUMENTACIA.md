### PRIEMEROVAC PRIETOKOV by dancejod
---
Program priemeruje vstupne denne prietoky po 7 dnoch a po roku a uklada ich do separatnych vystupov. Priemerny prietok sa vypise vedla prveho dna daneho obdobia.


### UZIVATELSKA DOKUMENTACIA
---
Na fungovanie skriptu su potrebne vstupne data, ktore budu ulozene ako <vstup.csv>. Vstupny subor musi obsahovat prave 6 stlpcov, zoradenych takto:

 1. databazove cislo,
 2. oznacenie typu dat,
 3. rok,
 4. mesiac,
 5. den,
 6. priemerny denny prietok [m3/s].

Ak vo vstupnom subore nie je prave 6 stlpcov, program spadne. Jednotlive stlpce budu oddelene ciarkou [,].
Vstupne data skript cita po riadku; ak je spravny, vytvoria sa 2 subory. Prvy subor <vystup_7dni.csv> obsahuje priemery prietokov za kazdych 7 dni, sedemdenny priemer je uvedeny stale pri prvom dni. Priemery z dni su postupne ukladane do zasobnika, ktory sa vyprazdni po siedmom dni. Ak nie je pocet riadkov v skripte delitelnych 7, na konci suboru sa vypriemeruje zvysny obsah zasobnika (zvysne dni). Druhy subor <vystup_rok.csv> obsahuje priemery prietokov za rok; rocny priemer je uvedeny stale pri prvom dni roka (1. 1.), a to okrem prveho riadka, ktory nemusi zacinat tymto datumom.

Na zaver program vytlaci spravu "Hotovo..." a uvedie minimalny a maximalny denny prietok vyskytujuci sa vo vstupnom subore.