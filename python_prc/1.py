arr = [1,2,3]
name = "Harry"
print(f"hello, {name}")
num = float(input())
print(round(num, 5))
print(f"{num:,}")
print(f"{num:.2f}")
print(5) if 4 else print(6)

# Conditional

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Harry":
        print("Slytherin")

# Loop
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
        
main()
# List
# Dictionary
    # - dictionary in list
#Exception
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print("x is", x)

#random
import random
from random import choice
from random import randint
from random import shuffle
print(choice([1,2]))
print(randint(1,10))
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)

#statistics
import statistics
print(statistics.mean([1,2,3,4,5,6,2]))

#sys
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(sys.argv[0])

for arg in sys.argv[2:]:
    print(arg)
#slice
#package

#api
#JSON
import requests
if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

import json
o = response.json()
print(json.dumps(o, indent=2))

for result in o["results"]:
    print(result["trackName"])

from hello import hello_world
hello_world()   #Only imported hello_world but main() is called as well

# __name__
if __name__ == "__main__":  # this part only executes whenever it's running in this program
    main()

# assert
# pytest
