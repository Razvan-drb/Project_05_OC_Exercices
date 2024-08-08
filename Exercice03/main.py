words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

list = []

voyelles = "aeoui"

for word in words:
    count = 0
    for letter in word:
        if letter.lower() in voyelles:
            count = count + 1
    list.append((word, count))
print(list)
