names = []
for _ in range(5):
    name = input("Enter a name")
    names.append(name)

lowercased = [name.lower() for name in names]
titlecased = [name.title()] for name in lowerecased]

invitations = ["Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for 