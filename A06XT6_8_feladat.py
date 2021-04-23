melymgh = ['a','á','o','ó','u','ú']
magasmgh = ['e','é','i','í','ö','ő','ü','ű']


s = input("Adja meg a fájl nevét: ")
while True:
    try:
        be = open(s,'r')
    except FileNotFoundError:
        print('A megadott fájl nem található!')
        s = input("Adjon meg egy új fájl nevet: ")