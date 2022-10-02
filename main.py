# Hassan Abdullah

def n_lower_chars(string):
    return sum([int(c.islower()) for c in string])
x = input("skirv ett ord: ")



print(n_lower_chars(x))
print(f"{n_lower_chars(x)}st små bokstäver")
