
tip = input("square or triangle?:   ")

kenar = []

if tip == "triangle":
    for x in range(1,4):
        kenar.append(int(input("{}th side".format(x))))

    for y in [kenar.count(max(kenar)), kenar.count(min(kenar))]:
        if y == 3:
            print("Eşkenar Üçgen")
            break
        
        elif y == 2:
            print("ikizkenar Üçgen")
            break 
    
elif tip == "square":
    for x in range(1,5):
        kenar.append(int(input("{}th side".format(x))))

    for y in [kenar.count(max(kenar)), kenar.count(min(kenar))]:
        if y == 4:
            print("kare")
            break

        elif kenar[0] == kenar[2] and kenar[1] == kenar[3]:
            print("Dikdörtgen")
            break

        else:
            print("Dörtgen")

else:

    print("Try again!")
