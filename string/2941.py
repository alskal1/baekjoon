
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()

for i in croatia:
    words = words.replace(i, " ")

print(len(words))