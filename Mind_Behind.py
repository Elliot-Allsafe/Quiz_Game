def run():
    Q1 = "How many Continents are there in the World?"
    Q2 = "How many Oceans are there in the World?"
    Q3 = "How many Countries are there in the World?"
    Q4 = "Which currency is Considered as International Currency?"
    Q5 = "How many Wonders are there in the World?"

    score = 0
    print(Q1)
    a1 = input("> ")
    if a1 == "7" or a1 == "Seven" or a1 == "seven":
        score += 1

    print(Q2)
    a2 = input("> ")
    if a2 == "7" or a2 == "Seven" or a2 == "seven":
        score += 1

    print(Q3)
    a3 = input("> ")
    if a3 == "195" or a3 == "One Ninty Five" or a3 == "one ninty five":
        score += 1

    print(Q4)
    a4 = input("> ")
    if a4 == "$" or a4 == "Dollar" or a4 == "dollar" or \
            a4 == "Dollars" or a4 == "dollars":
        score += 1

    print(Q5)
    a5 = input("> ")
    if a5 == "7" or a5 == "Seven" or a5 == "seven":
        score += 1

    print(str(score) + "/5")
    if score == 5:
        print("Fantastic!")
    elif 3 <= score < 5:
        print("Not Bad!")
    elif 3 > score >= 1:
        print("Go and Practice!")
    else:
        print("It's Shameful.")
