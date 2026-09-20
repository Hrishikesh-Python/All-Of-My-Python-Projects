import pyfiglet
import colorama
import time
import os


Player_Name = (input("Hello what's your name?"))

print()

print("Oh, nice name,", Player_Name )

print()

input("Press any key to continue")

print()

print("Well my name is,\n")

print()

print("HH   HH", "RRRRRR ", "IIIIIII", " SSSSS ", "HH   HH", "IIIIIII", "KK   KK", "EEEEEEE", " SSSSS ", "HH   HH", sep = "\t")
print("HH   HH", "RR   RR", "   II  ", "SS     ", "HH   HH", "   II  ", "KK  KK ", "EE     ", "SS     ", "HH   HH", sep = "\t")
print("HH   HH", "RR   RR", "   II  ", "SS     ", "HH   HH", "   II  ", "KK KK  ", "EE     ", "SS     ", "HH   HH", sep = "\t")
print("HHHHHHH", "RRRRRR ", "   II  ", " SSSSS ", "HHHHHHH", "   II  ", "KKKK   ", "EEEEEE ", " SSSSS ", "HHHHHHH", sep = "\t")
print("HH   HH", "RR RR  ", "   II  ", "     SS", "HH   HH", "   II  ", "KK KK  ", "EEE    ", "     SS", "HH   HH", sep = "\t")
print("HH   HH", "RR  RR ", "   II  ", "     SS", "HH   HH", "   II  ", "KK  KK ", "EE     ", "     SS", "HH   HH", sep = "\t")
print("HH   HH", "RR   RR", "IIIIIII", " SSSSS ", "HH   HH", "IIIIIII", "KK   KK", "EEEEEEE", " SSSSS ", "HH   HH", sep = "\t", end = "\n\r")

print()

input("Press any key to continue")

print("Here is the python logo: ")

print()

print()

print()

print()

from colorama import Fore, init

init(autoreset=True)

DOT = "● "

BLUE = Fore.BLUE

YELLOW = Fore.YELLOW

logo = [
"                BBBBBBBBB",
"              BBBBBBBBBBBBBB",
"            BBBBBBBBBBBBBBBBB",
"           BBBBBBBBBBBBBBBBBBB",
"           BBB   BBBBBBBBBBBBBB",
"           BB    BBBBBBBBBBBBBB",
"           BBB  BBBBBBBBBBBBBBB",
"           BBBBBBBBBBBBBBBBBBBB",
"           BBBBBBBBBBBBBBBBBBBB",
"            BBBBBBBBBBBBBBBBBBB",
"                     BBBBBBBBBB  YYY",
"    BBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYY",
"   BBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYY",
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYY",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYYY",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYYY",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYYY",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYYYYY",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB YYYYYYYYYYY",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBB  YYYYYYYYYYYY",
"BBBBBBBBBBBBBBB              YYYYYYYYYYYYY",
"BBBBBBBBBBB    YYYYYYYYYYYYYYYYYYYYYYYYYYY",
"BBBBBBBBBBB  YYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"BBBBBBBBBB  YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"BBBBBBBBBB YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
" BBBBBBBBB YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
" BBBBBBBBB YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
" BBBBBBBBBYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"  BBBBBBBBYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"   BBBBBBBYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"    BBBBB YYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"       B  YYYYYYYYYYY",
"          YYYYYYYYYYYYYYYYY",
"          YYYYYYYYYYYYYYYYY",
"          YYYYYYYYYYYYYYYYY",
"          YYYYYYYYYYYYYYYY YYYY",
"          YYYYYYYYYYYYYYY   YYY",
"           YYYYYYYYYYYYYY   YYY",
"           YYYYYYYYYYYYYYYYYYYY",
"            YYYYYYYYYYYYYYYYYY",
"             YYYYYYYYYYYYYYYY",
"                YYYYYYYYYY"
]

for row in logo:
    for pixel in row:
        if pixel == "B":
            print(BLUE + DOT, end="")
        elif pixel == "Y":
            print(YELLOW + DOT, end="")
        else:
            print("  ", end="")
    print()

print()

input("Press any key to continue")    



fonts = pyfiglet.FigletFont.getFonts()

for font in fonts:
    print("\nFONT:", font)
    print(pyfiglet.figlet_format("HI", font=font))

while True:
    Chosen_Font = input("Which font do you like the best from this?")

    if Chosen_Font in fonts:
        break

    else:

        print("That font doesn't exist. Please try again!")

print()

        
input("Press any key to continue")

os.system("clear")


print(pyfiglet.figlet_format("Ok, bye we will meet again!", font=Chosen_Font))


