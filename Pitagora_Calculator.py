import pitagora

while True:
    try:
        
        print("Digita 1 per TROVARE IPOTENUSA")
        print("Digita 2 per TROVARE CATETO MAGGIORE")
        print("Digita 3 per TROVARE CATETO MINORE")
        choose=int(input("Scegli: "))
        print()

        if choose==1:
            C=int(input("Inserisci CATETO MAGGIORE: "))
            c=int(input("Inserisci CATETO MINORE: "))
            print()
            alfa=pitagora.ip(C,c)
            print(alfa)
            print()
            print()
            print()

        if choose==2:
            c=int(input("Inserisci CATETO MINORE: "))
            ip=int(input("Inserisci IPOTENUSA: "))
            print()
            alfa=pitagora.C(ip,c)
            print(alfa)
            print()
            print()
            print()

        if choose==3:
            ip=int(input("Inserisci IPOTENUSA: "))
            C=int(input("Inserisci CATETO MAGGIORE: "))
            print()
            alfa=pitagora.c(ip,C)
            print(alfa)
            print()
            print()
            print()

    except ValueError:
        print()
        print("ERRORE...RICORDA DI SCRIVERE SOLO NUMERI")
        print()
        print()
        print()
