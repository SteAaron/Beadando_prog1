import sys

melymgh = ['a','á','o','ó','u','ú']
magasmgh = ['e','é','i','í','ö','ő','ü','ű']


s = input("Adja meg a fájl nevét: ")

try:
    file = open(s,'r',encoding='utf-8')
    kimely = open('mely.txt','w')
    kimagas = open('magas.txt','w')
    kivegyes = open('vegyes.txt','w')

    ls1 = [] #mély
    ls2 = [] #magas
    ls3 = [] #vegyes
    #ls4 = [] #egyéb

    for sor in file:
        line=sor.strip()

        #print(line)
        if ('a' or 'á' or 'o' or 'ó' or 'u' or 'ú') in line and ('e' or 'é' or 'i' or 'í' or 'ö' or 'ő' or 'ü' or 'ű') not in line:
            ls1.append(line)
        elif ('a' or 'á' or 'o' or 'ó' or 'u' or 'ú') not in line and ('e' or 'é' or 'i' or 'í' or 'ö' or 'ő' or 'ü' or 'ű') in line:
            ls2.append(line)
        elif ('a' or 'á' or 'o' or 'ó' or 'u' or 'ú') in line and ('e' or 'é' or 'i' or 'í' or 'ö' or 'ő' or 'ü' or 'ű') in line:
            ls3.append(line)
        # else:
        #     ls4.append(line)

    # print(ls1)
    # print(ls2)
    # print(ls3)
    # print(ls4)

    print(ls1, file = kimely)
    print(ls2, file = kimagas)
    print(ls3, file = kivegyes)

    file.close()
    kimely.close()
    kimagas.close()
    kivegyes.close()

except FileNotFoundError:
    print('A megadott fájl nem található!')
    s = input("Adjon meg egy új fájl nevet: ")

# if melymgh in szo and not magasmgh in szo:
#     print(sor, file=kimely)
# elif not melymgh in szo and magasmgh in szo:
#     print(sor, file=kimagas)
# elif melymgh in szo and magasmgh in szo:
#     print(sor, file=kivegyes)