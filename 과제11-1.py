scores= [('국어', 88), ('수학', 90), ('영어', 99), ('자연', 82)]

aligned = sorted(scores, key=lambda x: (x[1]))

print("정렬된 리스트:")
print(aligned)