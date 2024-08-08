"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Koštuříková
email: kosturikovap@gmail.com
discord: Pavla K
"""


import re
# import textů, ze kterých uživatel vybírá, z listu 'TEXTS'
from task_template import TEXTS

# registrovaní uživatelé
# slovník 'users': klíč = jméno uživatele, hodnota = heslo uživatele
users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

# vstup od uživatele - jméno = 'username' a heslo = 'password'
username = input("username: ")
password = input("password: ")
print(odd := "-" * 40)

# kontola správného jména a hesla ze slovníku 'users'
if users.get(username) != None and users[username] == password:
    print(f"Welcome to the app, {username}\nWe have {len(TEXTS)} texts to be analyzed.")
else:
    # v případě neregistovaného uživatele ukončení programu
    print("Unregistered user, terminating the program...")
    exit()
print(odd)

# vstup od uživatele, výběr textu z listu 'TEXTS' pomocí čísla 1 až délky listu 'TEXTS',
# uloženého do proměnné 'num'
num = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(odd)

# v případě chybného vstupu od uživatele, ukončení programu
if not num.isdigit():
    print("Input is not a number, terminating the program...")
    exit()
elif int(num) < 1 or int(num) > len(TEXTS):
    print("Number is not correct, terminating the program...")
    exit()

# vybrání konkrétního textu z listu 'TEXTS' a uložení do proměnné 'text'
# ze stringu 'text' převední do listu 'words'
num = int(num)
text = str(TEXTS[num-1])
words = text.split()
# print(words)

# 'words_only' = odstranění interpunkce z listu 'words'
words_only = [re.sub("[^A-Za-z0-9]", "", word) for word in words]

# 'word_count' - počet slov v listu 'words_only'
word_count = len(words_only)
print(f"There are {word_count} words in the selected text.")

title_count = 0     # počet slov v listu 'words_only' začínajících velkým písmenem
upper_count = 0     # počet slov v listu 'words_only' psaných velkými písmeny
lower_count = 0     # počet slov v listu 'words_only' psaných malými písmeny
number_count = 0    # počet čísel v listu 'words_only'
sum_number = 0      # součet všech čísel v listu 'words_only'
frequency = []      # četnost délek slov v listu 'word_only'

for word in words_only:
    if word.isalpha():
        title_count += int(word[0].isupper())
        upper_count += int(word.isupper())
        lower_count += int(word.islower())
    number_count += int(word.isnumeric())
    if word.isnumeric():
        sum_number += int(word)
    frequency.append(len(word))

print(f"There are {title_count} titlecase words.")
print(f"There are {upper_count} uppercase words.")
print(f"There are {lower_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"There sum of all the numbers {sum_number}.")
print(odd)

# graf četnosti délek slov v listu 'word_only'
print("LEN|", "OCCURENCES".center(16), "|NR.")
print(odd)
for length in range(1,max(frequency)+1):
    fr = frequency.count(length)
    star = "*" * fr
    if fr:
        print(f"{str(length).rjust(3)}|{star.ljust(18)}|{str(fr).ljust(0)}")

      