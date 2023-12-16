import random
from itertools import combinations

streets = ["Freudenweg", "Nobelstrasse", "Van Gogh Allee", "Gassenweg", "Hafenweg", "Postfach"]
first_names = ["Klaus", "Matthias", "Kurt", "Claudia", "Markus", "Paulus"]
last_names = ["Kinsky", "Müller", "Grandson", "Jefferson", "Washington", "von Wald"]

for i in range(10):
    i+1
    nr = random.randint(0, 65)
    print(random.choice(first_names)+" "+random.choice(last_names)+", "+random.choice(streets)+" "+str(nr))