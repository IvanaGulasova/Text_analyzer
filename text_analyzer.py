"""
projekt_1.py: první projekt do Engeto Online Python Akademie
autor: Ivana Gulasova
email: ivana.gulasova3@gmail.com
discort: IvanaG#9103 
"""

text1 = """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""

text2 = """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""

text3 = """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""

all_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = ("bob", "ann", "mike", "liz")
all_passwords = ("123", "pass123", "password123", "pass123")
section = "-" *40

user_name = input("Username: ")
password = input("Password: ")
print(section)

if user_name in all_users and all_users[user_name] == password:   
    print(f"Welcome to the app, {user_name}")
else:
    print("Unregistered user, terminating the program..")
    quit()

print("We have 3 texts to be analyzed.")
print(section)

def sum_words(text):
    return len(text.split())

def title_case(text):
    return sum(map(str.istitle, text.split()))

def upper_and_alpha(word):
    if str(word).isupper() and str(word).isalpha():
        return True
    else:
        return False
    
def upper_case(text):
    return sum(map(lambda x: upper_and_alpha(x), text.split()))

def lower_case(text):
    return sum(map(str.islower, text.split()))

def numeric_case(text):
    return sum(map(str.isdigit, text.split()))

def sum_all_numb(text):
    return sum(int(word) for word in text.split() if word.isdigit())

try:
    choice = int(input("Enter a number btw. 1 and 3 to select: "))
    print(section)
except:
    print("You did not enter a valid number, terminating the program..")
    quit()
if choice <1 or choice >3:
    print("You did not enter a valid number, terminating the program..")
    quit()

if choice == 1:
    text = text1
elif choice == 2:
    text = text2
elif choice == 3:
    text = text3

print(f"There are {sum_words(text)} words in the selected text.")          
print(f"The are {title_case(text)} titlecase words.")                     
print(f"There are {upper_case(text)} uppercase words.")
print(f"There are {lower_case(text)} lowercase words.")
print(f"There are {numeric_case(text)} numeric strings.") 
print(f"The sum of all the numbers {sum_all_numb(text)}.")    

print(section)
dict_of_len = {}
split_words = text.split()

for word in split_words:
    len_word = len(word.strip(",."))
    if len_word in dict_of_len:
        dict_of_len[len_word] += 1
    else:
        dict_of_len[len_word] = 1
    
sorted_dict = {k: dict_of_len[k] for k in sorted(dict_of_len)}
max = max(sorted_dict.values()) +2

chart_name = "LEN|".center(4) + "OCCURENCES".center(max) + "|NR".center(3)
print(chart_name)
print(section)

for k,v in sorted_dict.items():
    print(str(k).rjust(3) + "|" + str("*" *v).ljust(max) + "|" + str(v))