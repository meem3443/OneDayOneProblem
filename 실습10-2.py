import random

infile = open("numbers.txt", "w")

for i in range(10):
    number = random.randint(1, 100)
    infile.write(str(number) + "\n")

infile.close()