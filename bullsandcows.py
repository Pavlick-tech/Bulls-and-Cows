import random

def oddelovaciRadek():
    return print("-----------------------------------------------") 

print("Hi there!")
oddelovaciRadek()

digits = set(range(1,10))
firstdigit = random.randint(1, 9)
otherdigits = random.sample(digits - {firstdigit}, 3)
nahodneCislo = str(firstdigit) + ''.join(map(str, otherdigits))
print(nahodneCislo)

nahodneCisloList = [int(digit) for digit in str(nahodneCislo)]   

print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
oddelovaciRadek()

konecHry = bool(False)
pocetPokusu = 0
pocetNeplatnychPokusu = 0
while not konecHry:
    print("Enter a number:")
    odhadovaneCislo = input()

    if odhadovaneCislo.isdigit():

        if len(odhadovaneCislo) != 4:
            
            pocetNeplatnychPokusu += 1
            print("Not a valid guess. The guess must be a number with 4 unique digits.")
        
        else:
                
                if len(set(str(odhadovaneCislo)))<len(str(odhadovaneCislo)):
                
                    pocetNeplatnychPokusu += 1
                    print("Not a valid guess. Guess must not contain repeating digits.")
                
                else:

                    odhadovaneCisloList = [int(digit) for digit in str(odhadovaneCislo)] 
                    
                    pocetBulls = 0
                    pocetCows = 0

                    for i in range(len(odhadovaneCislo)):

                        if odhadovaneCisloList[i] == nahodneCisloList[i]:

                            pocetBulls +=1

                        if odhadovaneCisloList[i] != nahodneCisloList[i] and odhadovaneCisloList[i] in nahodneCisloList:
                            pocetCows +=1                              

                    if pocetBulls == 4:
                        pocetPokusu += 1
                        zprava = "Congratulations, you guessed a random number. Number of valid attempts : " + str(pocetPokusu) + ", number of invalid attempts: " + str(pocetNeplatnychPokusu)
                        print(zprava)
                        konecHry = bool(True)
                    else:
                        konecHry = bool(False)
                        pocetPokusu += 1
                        if pocetBulls > 1:
                            vysledekKola = str(pocetBulls) + " bulls, " 
                        else:
                            vysledekKola = str(pocetBulls) + " bull, "     

                        if pocetCows > 1:
                            vysledekKola += str(pocetCows) + " cows, " 
                        else:
                            vysledekKola += str(pocetCows) + " cow, "  

                        print(vysledekKola)
                        oddelovaciRadek()
    else:
        pocetNeplatnychPokusu += 1
        print("Not a valid guess. The guess must be a number with 4 unique digits.")        






 