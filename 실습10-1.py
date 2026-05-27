infile = open("input.txt", "r")

words = infile.read().split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("가장 긴 단어는", longest, "입니다.")

infile.close()