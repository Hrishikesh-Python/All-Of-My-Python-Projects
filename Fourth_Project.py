import time
import random
Pass_1 = "Fail"
Pass_2 = "Fail"
Pass_3 = "Fail"
Pass_4 = "Fail"
Time_Limit_1 = 20
Time_Limit_2 = 17.5
Time_Limit_3 = 15
Time_Limit_4 = 10
def Check_For_Vowels(Word_To_Check):
    Vowel_Count = 0
    for letter in Word_To_Check.lower():
        if letter in "aeiou":
            Vowel_Count += 1
    return Vowel_Count


print("==========================================================")
print("Welcome to the challenge:    The Impossible Word Challenge")
print("==========================================================")

print()
time.sleep(2)
print("Warning: Contains too many insults, if you are sensitive to any of this please leave immediately. If you are not sensitive, then many many apologies in adavnce!")
print()
time.sleep(2)
Intro_choice = input("Type 'SKIP' to fast-forward to the 1st question, or press ENTER to watch the intro: ").lower()
print()
time.sleep(2)
print("Please wait, this might take a while to load.....")
Wait_Period = random.randint(1,10)
time.sleep(Wait_Period)
print()
if Intro_choice != "skip":
    print()
    input("Press ENTER to continue!")
    print()
    time.sleep(3)
    print("       ERROR 404:      ")
    print("COMMON SENSE NOT FOUND  ")
    print()
    time.sleep(2)
    print("HAHAHA")
    print()
    print("Think you have a functioning brain?")
    print()
    time.sleep(2)
    print("Think again.")
    print()
    time.sleep(2)
    print("You will face 4 increasingly difficult challenges......")
    print()
    time.sleep(1)
    print("One mistake. One failure. INFINITE SHAME.")
    print()
    time.sleep(2)
    print("The rules are simple:")
    print()
    time.sleep(1)
    print("Follow EVERY instruction.")
    print()
    time.sleep(1)
    print("Answer as FAST as possible.")
    print()
    time.sleep(1)
    print("And whatever you do... DON'T EMBARRASS YOURSELF.")
    print()
    time.sleep(3)
    input("Press ENTER if you dare...")
    print()
    print("Wait, just one moment......")
    print()
    print("Your brain called, it wants to quit. But let us cotinue as you insist")
    print()
time.sleep(5)    
input("Type ENTER to start (This time for real) ")
print()
Start = time.time()
Answer_1 = str(input("The first and easieast challenge: \n Enter a word with EXACTLY 6 letters and EXACTLY 3 vowels.")).strip()
End = time.time()
Elapsed = End - Start
Vowels = Check_For_Vowels (Answer_1)
print()
if not Answer_1.isalpha():
    print("ARE YOU KIDDING ME? THAT IS NOT EVEN A WORD!")
elif len(Answer_1) != 6:
    print("I SAID SIX LETTERS CAN YOU COUNT?")
elif Vowels < 3:
    print("ARE YOU TRYING TO SCAM ME?? WHERE ARE THE VOWELS??")
elif Vowels > 3:
    print("ARE YOU KIDDING ME? I SAID 3!! ARE YOU TRYING TO SHOW OFF YOUR SKILL? BECAUSE IF YOU ARE, YOU ARE NOT SUCCEEDING!!!")
else:
    print("Fine, Congratulations! You passed the first question! Don't get too excited")
    if Elapsed < Time_Limit_1:
        Pass_1 = "Pass"
print()
print("You took", round(Elapsed, 2), "seconds!")
print()
if Elapsed > 15:
    print("BUT SERIOUSLY, WERE YOU THINKING FOR AN ENTIRE CENTURY?")
elif Elapsed > 7:
    print("BUT SERIOUSLY, DID YOU FALL ASLEEP MID-QUESTION?")
elif Elapsed < 3:
    print("BUT SERIOUSLY, YOU WERE SUSPICIOUSLY FAST. WERE YOU EVEN THINKING?")
else:
    print("FINALLY. THE BRAIN HAS BOOTED UP.")
time.sleep(5)
print()
Start = time.time()
Answer_2 = str(input("The second challenge: \n Enter a word with 6 letters, starting with S, having two vowels, and ending with N.")).strip()
End = time.time()
Elapsed = End - Start
Vowels = Check_For_Vowels(Answer_2)
if Answer_2.isalpha():
    if len(Answer_2) == 6:
        if Answer_2[0].lower() == "s":
            if Answer_2[-1].lower() == "n":
                if Vowels == 2:
                    print("Fine. You actually passed.")
                    if Elapsed < Time_Limit_2:
                        Pass_2 = "Pass"
                else:
                    print("TWO VOWELS! IS THAT TOO MUCH TO ASK?")
            else:
                print("IT HAS TO END WITH N!")
        else:
            print("START WITH S! NOT WHATEVER THAT WAS!")
    else:
        print("SIX LETTERS. COUNT THEM!")
else:
    print("LETTERS ONLY! WHAT IS THIS, A PASSWORD?")
print("You took", round(Elapsed, 2), "seconds!")
if Elapsed > 15:
    print("DID YOU WRITE A WHOLE NOVEL BEFORE ANSWERING?")
elif Elapsed > 7:
    print("YOUR BRAIN IS RUNNING ON DIAL-UP.")
elif Elapsed < 3:
    print("SUSPICIOUSLY FAST. CHEATER?")
else:
    print("CONGRATULATIONS. YOU HAVE BASIC REFLEXES.")
time.sleep(5)
print()
Start = time.time()
Answer_3 = str(input("The third challenge: \n Enter a word with an even number of letters and exactly 2 vowels")).strip()
End = time.time()
Elapsed = End - Start
Vowels = Check_For_Vowels(Answer_3)
if not Answer_3.isalpha():
    print("DID YOUR KEYBOARD HAVE A SEIZURE? I ASKED FOR A WORD, NOT YOUR ENTIRE KEYBOARD!!!")
    time.sleep(8)
elif len(Answer_3) > 6:
    print("ARE YOU TRYING TO WASTE MY TIME???? CAN'T YOU GIVE A SHORTER ANSWER?? NOT WORTH MY TIME!!!")
elif len(Answer_3) % 2 != 0:
    print("I SAID EVEN NUMBER OF LETTERS!!! NOT EVEN YOUR ANSWER IS EVEN!!!")
elif Vowels != 2:
    print("YOU HAD ONE JOB. TWO LETTERS. TWO!")
else: 
    print("Congratulations you have done the impossible yet again!")
    if Elapsed < Time_Limit_3:
                
            Pass_3= "Pass"
print("You took", round(Elapsed, 2), "seconds!")
if Elapsed > 15:
    print("BUT SERIOUSLY, WERE YOU THINKING FOR AN ENTIRE CENTURY?")
elif Elapsed > 7:
    print("BUT SERIOUSLY, DID YOU FALL ASLEEP MID-QUESTION?")
elif Elapsed < 3:
    print("BUT SERIOUSLY, YOU WERE SUSPICIOUSLY FAST. WERE YOU EVEN THINKING?")
else:
    print("FINALLY. THE BRAIN HAS BOOTED UP.")
time.sleep(5)
print()
Start = time.time()
Answer_4 = str(input("The Fourth Challenge: \n Enter a 10-letter word with 4 vowels, starting with B, ending with E, and containing no repeated letters.")).strip()
End = time.time()
Elapsed = End - Start
Vowels = Check_For_Vowels(Answer_4)
if not Answer_4.isalpha():
    print("CONGRATULATIoNS! YOU HAVE INVENTED A NEW LANGUAGE. TOO BAD IT'S WRONG!")
elif len(Answer_4) != 10:
    print("DID YOU COUNT WITH YOUR TOES AND STILL FAIL??? COUNTING IS FREE, YOU KNOW.")
elif Vowels != 4:
    print("FOUR VOWELS! NOT A VOWEL SHORTAGE! FOUR VOWELS. THIS ISN'T A VOWEL-FREE DIET!")
elif Answer_4[0].lower() != "b":
    print("START WITH b. NOT", Answer_4[-1], "! EVEN YOUR BRAIN CAN START PROPERLY ( I DON'T THINK SO!!!)")
elif not Answer_4.lower().endswith("e"):
    print("THE LETTER E WAS RIGHT THERE. RIGHT THERE!")
elif len(set(Answer_4.lower())) != len(Answer_4):
    Repeated_Letters = int(len(Answer_4))  - int(len(set(Answer_4.lower())))
    print("DID DISCOVER THE COPY-PASTE BUTTON OR SOMETHING? SERIOUSLY? ", str(Repeated_Letters), " REPEATED LETTERS?💀")
else:
    print("I THINK YOU ARE CHEATING!")
    if Elapsed < Time_Limit_4:
        Pass_4 = "Pass"
print("You took", round(Elapsed, 2), "seconds!")
if Elapsed > 15:
    print("DID YOU WRITE A WHOLE NOVEL BEFORE ANSWERING?")
elif Elapsed > 7:
    print("YOUR BRAIN IS RUNNING ON DIAL-UP.")
elif Elapsed < 3:
    print("SUSPICIOUSLY FAST. CHEATER?")
else:
    print("CONGRATULATIONS. YOU HAVE BASIC REFLEXES.")
if Pass_1 == "Pass" and Pass_2 == "Pass" and Pass_3 == "Pass" and Pass_4 == "Pass" :
    print("Congratulations! You have completed the impossible challenge which only a few people have done before!")
    print()
    time.sleep(3)
    Final_Response = input('Type the word "WINNER" to claim your victory!').strip()
    time.sleep(3)
    if Final_Response == "WINNER" :
        print("Congratulations. You have successfully wasted your time. Thank you for playing.")
    else:
        print("YOU SURVIVED FOUR LEVELS JUST TO FAIL THE LAST ONE! WHAT IS WRONG WITH YOU??")
    print("Anyway here are the answers: \n Answer 1:  \n    Animal \n    Banana \n    Guitar \n    Shadow")
    time.sleep(2)
    print()
    print("\n\n\n Answer 2: \n    Salmon \n    Strain \n    Spoken \n    Screen")
    time.sleep(2)
    print()
    print("\n\n\n Answer 3: \n    Soap \n    Twelve \n    Planet \n    Stream")
    time.sleep(2)
    print()
    print("\n\n\n Answer 4: \n    Bichromate \n    Brickhouse \n    Brickhouse \n    Bisulphate")
else:
    print("I'm sorry to say that you have failed the challenge. Please try again next time!")
Random_1 = random.randint(1,59)
Random_2 = random.randint(1,59)
Random_3 = random.randint(1,59)
Random_4 = random.randint(1,59)
print("Ok, pick your preferred slot for meeting me the following Wednesday (A/B/C/D)")
print("A. " ,Random_1, "  minutes past midnight", "B." ,Random_2, " minutes before sunrise", sep='\t'); 
print("C. " ,Random_3, "  minutes before noon  ",  "D." , Random_4, " minutes after sunset", sep='\t');
Appointment = input('Select your slot (A/B/C/D)\n').strip()
if Appointment == "A":
    print("Careful, I may be sleepy.")
elif Appointment == "B":
    print("Warning,  I may not be available")
elif Appointment == "C":
    print("Beware, I may be hangry.")
elif Appointment == "D":
    print("Caution, I may be tired.")
else:
    print("SERIOUSLY? I EVEN GAVE YOU A BUNCH OF OPTIONS! YOU JUST HAD TO TYPE ONE LETTER! ONE!")
print()
time.sleep(5)
print("Good luck!")
print()
time.sleep(2)
print("Bye for now!!!!")


    

















