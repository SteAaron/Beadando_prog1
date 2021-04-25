melymgh = ['a','á','o','ó','u','ú']
magasmgh = ['e','é','i','í','ö','ő','ü','ű']


s = input("Adja meg a fájl nevét: ")
while True:
    try:
        be = open(s,'r')
        kimely = open('mely.txt','w')
        kimagas = open('magas.txt','w')
        kivegyes = open('vegyes.txt','w')

        for sor in be:
            # l=sor.rstrip('\n')
            for szo in sor:
                if melymgh in szo and magasmgh not in szo:
                    print(sor, file=kimely)
                elif melymgh not in szo and magasmgh in szo:
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

# for sor in be:
#     #l=sor.rstrip('\n')
#     if mely in sor and magas not in sor:
#         print(sor,file=kimely)
#     elif mely not in sor and magas in sor:
#         print(sor,file=kimagas)
#     elif mely in sor and magas in sor:
#         print(sor,file=kivegyes)
#
# be.close()
# kimely.close()
# kimagas.close()
# kivegyes.close()