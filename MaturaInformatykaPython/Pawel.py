##########################################################################################
file = open('liczby.txt', 'r')
lines = file.readlines()
file1 = open("trojki.txt", "a")
file1.truncate(0)
##########################################################################################
#4.1 
print("--------------------------------------------------------------------------------")
print("zadanie 4.1: ")
count1 = 0
pierwsza = False
for i in lines:
    if(i[0] == i[-2]):
        if(pierwsza == False):
            print("Pierwsza napotkana liczba, ktorej cyfry pierwsza i ostatnia sa takie same: ", i)
            pierwsza = True
        count1 += 1
        
print("Ilosc takich liczb: ", count1)
print("\n")
##########################################################################################
#4.2
print("--------------------------------------------------------------------------------")
print("zadanie 4.2: ")
def RozlozCos(cos):
    czynniki = []
    k = 2
    while cos != 1:
        while cos % k == 0:
            cos //= k
            czynniki.append(k)
        k += 1
    
    return czynniki
#4.2a
max = 0
liczba = 0
for i in lines:
    a = RozlozCos(int(i.strip()))
    if(len(a) > max):
        max = len(a)
        liczba = int(i.strip())
print("Liczba, ktora ma najwiecej czynnikow pierwszych: ", liczba, "\nIlosc tych czynnikow: ", max)



#4.2b
max1 = 0
liczba1 = 0
for i in lines:
    a = int(i.strip())
    
    if len(set(RozlozCos(a))) > max1:
        max1 = len(set(RozlozCos(a)))
        liczba1 = a

print("\nLiczba, ktora ma w rozkladzie najwiecej roznych czynnikow: ", liczba1, "\nIlosc tych czynnikow: ", max1)
#################################################################################
#4.3
print("\n")
print("--------------------------------------------------------------------------------")
print("zadanie 4.3: ")

trzy= 0
piec = 0

#4.3a
for a1 in lines:
    x = int(a1.strip())
    for a2 in lines:
        if(x % int(a2.strip()) == 0):
            y = int(a2.strip())
            for a3 in lines:
                if(y % int(a3.strip()) == 0):
                    z = int(a3.strip())
                    if(x != y and y != z and z != x):
                        file1.write(str(x) + " " + str(y) + " " + str(z) + "\n")
                        trzy += 1
print("Liczba trojek w pliku: ", trzy,"\n")

#4.3b
for a1 in lines:
    u = int(a1.strip())
    for a2 in lines:
        if(u % int(a2.strip())) == 0:
            w = int(a2.strip())
            for a3 in lines:
                if(w % int(a3.strip()) == 0):
                    x = int(a3.strip())
                    for a4 in lines:
                        if(x % int(a4.strip()) == 0):
                            y = int(a4.strip())
                            for a5 in lines:
                                if(y % int(a5.strip()) == 0):
                                    z = int(a5.strip())
                                    if(u != w and u != x and u != y and u != z and w != x and w != y and w != z and x != y and x != z and y != z):
                                        piec += 1
print("Liczba piątek w pliku: ", piec)
##########################################################################################
