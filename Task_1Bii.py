def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for i in name1:
        if i in name2:
            name2 = name2.replace(i, "", 1)
            name1 = name1.replace(i, "", 1)

    count = len(name1) + len(name2)

    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index < 0:
            index = len(flames) - 1
        flames.pop(index)

    if flames[0] == "F":
        return "Friend"
    elif flames[0] == "L":
        return "Love"
    elif flames[0] == "A":
        return "Affection"
    elif flames[0] == "M":
        return "Marriage"
    elif flames[0] == "E":
        return "Enemy"
    elif flames[0] == "S":
        return "Sister"

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

print("The relationship between", name1, "and", name2, "is", calculate_flames(name1, name2))
