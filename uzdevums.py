guesswho = 4
i = 0
while i < 1:
    vert = float(input("uzmini skaitli"))
    if vert == guesswho:
        print("uzmineji")
        i = 1
    elif vert > guesswho:
        print("mazaks")
    else:
            print("lielaks")