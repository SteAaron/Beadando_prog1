import sys

melymgh = ['a','á','o','ó','u','ú']
magasmgh = ['e','é','i','í','ö','ő','ü','ű']


s = input("Adja meg a fájl nevét: ")

try:
    file = open(s,'r',encoding='utf-8')
    kimely = open('mely.txt','w')
    kimagas = open('magas.txt','w')
    kivegyes = open('vegyes.txt','w')

    for sor in file:
        line=sor.strip()
        for szo in line:
            if melymgh in szo and not magasmgh in szo:
                print(sor, file=kimely)
            elif not melymgh in szo and magasmgh in szo:
                print(sor, file=kimagas)
            elif melymgh in szo and magasmgh in szo:
                print(sor, file=kivegyes)


    be.close()
    kimely.close()
    kimagas.close()
    kivegyes.close()

except FileNotFoundError:
    print('A megadott fájl nem található!')
    s = input("Adjon meg egy új fájl nevet: ")

