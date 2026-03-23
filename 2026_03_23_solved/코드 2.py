sentence = list(input())

sentence[1] = "a"
sentence[-2] = "a"

str = ""

for i in sentence:
    str = str + i
print(str)