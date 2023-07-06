word = input("Dame una palabra:  ")

letter_counter = {}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] =1

print(f"Tu palabra tiene {len(word)} Letras")

for letter in letter_counter:
    print(letter, letter_counter[letter])
